function handler(event) {
    const request = event.request;
    const uri = request.uri;

    if (uri === "/posts/index.html" || uri === "/posts" || uri === "/posts/" || uri === "/blog" || uri === "/blog/") {
        return {
            statusCode: 301,
            headers: { "location": { "value": "/index.html" } },
        };
    }

    if (uri === "/rss.xml") {
        return {
            statusCode: 301,
            headers: { "location": { "value": "/feed.xml" } },
        };
    }

    // Old posts were aliased under /blog, but we want to redirect to the new /posts/
    if (uri.startsWith("/blog/")) {
        let suffix = "";
        if (!uri.endsWith(".html")) {
            suffix = ".html";
        }
        return {
            statusCode: 301,
            headers: { "location": { "value": uri.replace("/blog/", "/posts/") + suffix } },
        };
    }

    // Match anything in /posts without the .html suffix and redirect there
    if (uri.startsWith("/posts/") && !uri.endsWith(".html")) {
        return {
            statusCode: 301,
            headers: {
                "location": { "value": uri + ".html" },
            },
        };
    }

    return request;
}
