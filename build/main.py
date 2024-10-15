import markdown
from markdown.blockprocessors import BlockProcessor
from markdown.extensions import Extension
from markdown.postprocessors import Postprocessor
from markdown.treeprocessors import Treeprocessor
import os.path
import sys
import xml.etree.ElementTree as etree

class DocumentAttributes(object):
    def __init__(self):
        self.title = None

class ExtractTitleBlockProcessor(BlockProcessor):
    def __init__(self, parser, attrs):
        super().__init__(parser)
        self.doc_attrs = attrs

    def test(self, parent, block):
        return block.startswith('__TITLE__')

    def run(self, parent, blocks):
        block = blocks.pop(0)
        lines = block.split('\n')
        
        title = lines[0][len('__TITLE__'):].strip()
        self.doc_attrs.title = title
        subtitles = []
        
        for line in lines[1:]:
            if line.startswith('__SUBTITLE__'):
                subtitles.append(line[len('__SUBTITLE__'):].strip())
            else:
                break

        wrapper = etree.SubElement(parent, 'div')
        wrapper.set('class', 'title-underline')
        
        title_elem = etree.SubElement(wrapper, 'h1')
        title_elem.text = title
        
        for subtitle in subtitles:
            subtitle_elem = etree.SubElement(wrapper, 'p')
            subtitle_elem.set('class', 'subtitle')
            subtitle_elem.text = subtitle

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
    def __init__(self, md, attrs):
        super().__init__(md)
        self.doc_attrs = attrs

    def run(self, text):
        with open("blog/src/template.html", "r") as file:
            template = file.read()
        return template.replace('$$BODY$$', text).replace('$$TITLE$$', self.doc_attrs.title)

class BlogExtension(Extension):
    def __init__(self):
        self.doc_attrs = DocumentAttributes()

    def extendMarkdown(self, md):
        md.parser.blockprocessors.register(ExtractTitleBlockProcessor(md.parser, self.doc_attrs), 'title', 175)
        md.treeprocessors.register(WrapInArticleTreeProcessor(md), 'article', 100)
        md.postprocessors.register(ApplyTemplatePostprocesor(md, self.doc_attrs), 'template', 100)

def build_post(path):
    output_file = path.replace("blog/src/posts/", "blog/dist/posts/").replace(".md", ".html")
    print(f"Compiling {path} to {output_file}...")

    with open(path, "r") as file:
        content = file.read()

    html = markdown.markdown(content, extensions=[BlogExtension(), 'footnotes'])

    with open(output_file, "w") as file:
        file.write(html)

def build_all():
    for root, dirs, files in os.walk("blog/src/posts/"):
        for file in files:
            if file.endswith(".md"):
                build_post(os.path.join(root, file))

def main(args):
    if args[0] == "dev":
        # Start a web server on port 8000 that serves the blog posts in a daemon thread
        import http.server
        import threading

        server = http.server.HTTPServer(('localhost', 8000), lambda *args: http.server.SimpleHTTPRequestHandler(*args, directory='blog/dist/'))
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

        class TemplateHandler(FileSystemEventHandler):
            def on_modified(self, event):
                build_all()

        observer = Observer()
        observer.schedule(PostHandler(), path='blog/src/posts/', recursive=False)
        observer.schedule(TemplateHandler(), path='blog/src/template.html', recursive=False)
        observer.start()

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
