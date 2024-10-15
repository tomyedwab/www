import markdown
from markdown.blockprocessors import BlockProcessor
from markdown.extensions import Extension
from markdown.postprocessors import Postprocessor
from markdown.treeprocessors import Treeprocessor
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

with open("blog/src/posts/cursor-review.md", "r") as file:
    content = file.read()

html = markdown.markdown(content, extensions=[BlogExtension(), 'footnotes'])

with open("blog/dist/posts/cursor-review.html", "w") as file:
    file.write(html)