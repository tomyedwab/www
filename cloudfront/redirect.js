function handler(event) {
    const request = event.request;
    const uri = request.uri;

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
