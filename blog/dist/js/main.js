const annotations = [];

class Annotation {
    constructor(annotationPane, footnote, content, targetRef, footnoteId) {
        this.annotationPane = annotationPane;
        this.wrapper = footnote;
        this.content = content;
        this.height = this.content.offsetHeight;
        this.targetRef = targetRef;
        this.footnoteId = footnoteId;
        this.isInSidebar = false;
        this.wrapper.style.height = "auto";
        this.wrapper.style.transition = "height 1s";
        this.wrapper.style.overflow = "hidden";
        this.wrapper.style.position = "relative";

        this.content.style.transition = "none";
        this.content.style.height = "auto";
        this.content.style.top = "0px";
        this.content.style.left = "0px";
    }

    startMoveToSidebar() {
        this.wrapper.style.height = "0px";
        if (this.targetRef) {
            this.targetRef.children[0].href = `#innerref:${this.footnoteId}`;
        }
    }

    endMoveToSidebar(minTop) {
        let targetTop = this.targetRef ? this.targetRef.offsetTop : 0;
        if (targetTop < minTop) {
            targetTop = minTop;
        }
        if (!this.isInSidebar) {
            this.content.remove();
            this.content.style.clipPath = `rect(0 0 0 100%)`;
        }
        this.content.style.position = "absolute";
        this.content.style.transition = "clip-path 0.5s, top 0.5s";
        this.content.style.top = `${targetTop}px`;
        if (!this.isInSidebar) {
            this.annotationPane.appendChild(this.content);
            this.isInSidebar = true;
        }
        this.height = this.content.offsetHeight;
        setTimeout(() => {
            this.content.style.height = "auto";
            this.content.style.clipPath = `rect(0 0 ${this.height}px 100%)`;
        }, 10);
        return targetTop + this.height;
    }

    moveToFooter() {
        if (this.isInSidebar) {
            this.wrapper.style.height = "auto";
            if (this.targetRef) {
                this.targetRef.children[0].href = `#fn:${this.footnoteId}`;
            }
            this.content.remove();
            this.content.style.top = 0;
            this.content.style.position = "relative";
            this.wrapper.appendChild(this.content);
            this.isInSidebar = false;
        }
    }
}

const debounce = (func, delay) => {
    let timeoutId;
    return (...args) => {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => func(...args), delay);
    };
};

const handleResize = debounce(() => {
    // TODO: Decide whether to show annotation sidebar
    if (window.innerWidth > 870) {
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
    } else {
        annotations.forEach(annotation => {
            annotation.moveToFooter();
        });
    }
}, 100);

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
        content.id = `innerref:${footnoteId}`;
        annotations.push(new Annotation(annotationPane, footnote, content, footnoteRef, footnoteId));
    });
    document.querySelectorAll("p.pop-out").forEach(popout => {
        const content = document.createElement("div");
        content.innerHTML = popout.innerHTML;
        popout.innerHTML = "";
        popout.appendChild(content);
        annotations.push(new Annotation(annotationPane, popout, content, null, null));
    });

    setTimeout(() => {
        handleResize();
    }, 0);

    window.addEventListener("resize", () => {
        handleResize();
    });
});
