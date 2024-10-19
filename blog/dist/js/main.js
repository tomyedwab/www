const annotations = [];

class Annotation {
    constructor(annotationPane, footnote, content, targetRef) {
        this.annotationPane = annotationPane;
        this.wrapper = footnote;
        this.content = content;
        this.height = this.content.offsetHeight;
        this.targetRef = targetRef;
        this.wrapper.style.height = `${this.height}px`;
        this.wrapper.style.transition = "height 1s";
        this.wrapper.style.overflow = "hidden";
        this.wrapper.style.position = "relative";

        this.content.style.transition = "none";
        this.content.style.height = `${this.height}px`;
        this.content.style.position = "absolute";
        this.content.style.top = "0px";
        this.content.style.left = "0px";
    }

    startMoveToSidebar() {
        this.wrapper.style.height = "0px";
    }

    endMoveToSidebar(minTop) {
        let targetTop = this.targetRef.offsetTop;
        if (targetTop < minTop) {
            targetTop = minTop;
        }
        this.content.remove();
        this.content.style.height = "0px";
        this.content.style.transition = "height 0.5s";
        this.content.style.top = `${targetTop}px`;
        this.annotationPane.appendChild(this.content);
        setTimeout(() => {
            this.content.style.height = `${this.height}px`;
        }, 10);
        return targetTop + this.height;
    }
}

function handleResize() {
    // TODO: Decide whether to show annotation sidebar
    annotations.forEach(annotation => {
        annotation.startMoveToSidebar();
    });
    // TODO: Sort the annotations by target position on the page
    setTimeout(() => {
        let top = 0;
        annotations.forEach(annotation => {
            top = annotation.endMoveToSidebar(top);
        });
    }, 1000);
}

document.addEventListener("DOMContentLoaded", () => {
    const article = document.querySelector("article");
    console.log("article", article);
    const annotationPane = document.createElement("div");
    annotationPane.classList.add("annotation-pane");
    article.appendChild(annotationPane);

    document.querySelectorAll("div.footnote ol li").forEach(footnote => {
        const footnoteId = footnote.id.split(":")[1];
        const footnoteRef = document.getElementById(`fnref:${footnoteId}`);
        const content = footnote.children[0];
        annotations.push(new Annotation(annotationPane, footnote, content, footnoteRef));
    });

    setTimeout(() => {
        handleResize();
    }, 0);
});