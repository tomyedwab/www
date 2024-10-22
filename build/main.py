import markdown
from markdown.blockprocessors import BlockProcessor
from markdown.extensions import Extension
from markdown.postprocessors import Postprocessor
from markdown.treeprocessors import Treeprocessor
import os.path
import sys
import xml.etree.ElementTree as etree

PostMetadatas = {}

class WrapInArticleTreeProcessor(Treeprocessor):
    def run(self, root):
        body_els = [
            child for child in root if child.tag != 'div' or child.get('class') != 'title-underline'
        ]
        article = etree.SubElement(root, 'article')
        for child in body_els:
            root.remove(child)
            article.append(child)

class ApplyTemplatePostprocesor(Postprocessor):
    def __init__(self, md, post_uri):
        super().__init__(md)
        self.post_uri = post_uri

    def run(self, text):
        PostMetadatas[self.post_uri] = {
            "uri": self.post_uri,
            "title": self.md.Meta['title'][0],
            "subtitle": self.md.Meta['subtitle'][0],
            "description": self.md.Meta['description'][0],
        }
        with open("blog/src/template.html", "r") as file:
            template = file.read()
        return (
            template
            .replace('$$ROOT$$', "..")
            .replace('$$BODY$$', text)
            .replace('$$TITLE$$', self.md.Meta['title'][0])
            .replace('$$SUBTITLE$$', self.md.Meta['subtitle'][0])
            .replace('$$DESCRIPTION$$', self.md.Meta['description'][0])
        )

class BlogExtension(Extension):
    def __init__(self, post_uri):
        self.post_uri = post_uri

    def extendMarkdown(self, md):
        md.treeprocessors.register(WrapInArticleTreeProcessor(md), 'article', 100)
        md.postprocessors.register(ApplyTemplatePostprocesor(md, self.post_uri), 'template', 100)

def build_post(path):
    output_file = path.replace("blog/src/posts/", "blog/dist/posts/").replace(".md", ".html")
    print(f"Compiling {path} to {output_file}...")

    with open(path, "r") as file:
        content = file.read()

    html = markdown.markdown(content, extensions=[BlogExtension(output_file[10:]), 'footnotes', 'meta', 'attr_list'])

    with open(output_file, "w") as file:
        file.write(html)

def build_index():
    post_uris = sorted(PostMetadatas.keys(), reverse=True)
    text = "<ul class=\"post-list\">\n"
    for post_uri in post_uris:
        post_metadata = PostMetadatas[post_uri]
        text += f"<li><h2><a href=\"{post_metadata['uri']}\">{post_metadata['title']}</a></h2><p class=\"subtitle\">{post_metadata['subtitle']}</p><p>{post_metadata['description']}</p></li>\n"
    text += "</ul>\n"

    with open("blog/src/template.html", "r") as file:
        template = file.read()
    html = (
        template
        .replace('$$ROOT$$', ".")
        .replace('$$BODY$$', text)
        .replace('$$TITLE$$', "History of posts")
        .replace('$$SUBTITLE$$', "")
        .replace('$$DESCRIPTION$$', "History of blog posts on the Arguing with Algorithms blog.")
    )
    with open("blog/dist/index.html", "w") as file:
        file.write(html)

def build_all():
    for root, dirs, files in os.walk("blog/src/posts/"):
        for file in files:
            if file.endswith(".md"):
                build_post(os.path.join(root, file))
    build_index()

def main(args):
    if args[0] == "dev":
        # Start a web server on port 8000 that serves the blog posts in a daemon thread
        import http.server
        import threading

        server = http.server.HTTPServer(('0.0.0.0', 8000), lambda *args: http.server.SimpleHTTPRequestHandler(*args, directory='blog/dist/'))
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()

        print("Server started at http://localhost:8000")

        import time
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler

        class PostHandler(FileSystemEventHandler):
            def on_modified(self, event):
                if event.src_path.endswith('.md') and 'blog/src/posts/' in event.src_path:
                    build_post(event.src_path)
                    build_index()

        class TemplateHandler(FileSystemEventHandler):
            def on_modified(self, event):
                build_all()

        observer = Observer()
        observer.schedule(PostHandler(), path='blog/src/posts/', recursive=False)
        observer.schedule(TemplateHandler(), path='blog/src/template.html', recursive=False)
        observer.start()

        build_all()
        print("Watching for changes in blog/src/posts/...")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

    elif args[0] == "build":
        build_all()

    elif len(args) == 1:
        build_post(args[0])
    else:
        print("Usage: build.py <path/to/post.md>")

if __name__ == "__main__":
    main(sys.argv[1:])
