// pop up 




// ==UserScript==
// @name         Editable Network Logger
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Intercept and edit request body before sending
// @match        https://www.tirangagames.top/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    const targetUrl = 'https://tirangaapi.com/api/webapi/GetNoaverageEmerdList';

    function interceptAndEditRequest(method, url, body, sendRequest) {
        if (url.includes(targetUrl)) {
            console.log('Original Request Body:', body);
            let editedBody = prompt('Edit the request body:', JSON.stringify(body));
            if (editedBody !== null) {
                try {
                    editedBody = JSON.parse(editedBody);
                    console.log('Edited Request Body:', editedBody);
                } catch (e) {
                    console.error('Invalid JSON:', e);
                    alert('Invalid JSON. Sending original request body.');
                    editedBody = body;
                }
            } else {
                editedBody = body;
            }
            sendRequest(JSON.stringify(editedBody));
        } else {
            sendRequest(body);
        }
    }

    // Intercept XMLHttpRequest
    const originalXhrOpen = XMLHttpRequest.prototype.open;
    XMLHttpRequest.prototype.open = function(method, url, async, user, password) {
        this._url = url;
        this._method = method;
        originalXhrOpen.apply(this, arguments);
    };

    const originalXhrSend = XMLHttpRequest.prototype.send;
    XMLHttpRequest.prototype.send = function(body) {
        if (this._url) {
            interceptAndEditRequest(this._method, this._url, JSON.parse(body), editedBody => {
                originalXhrSend.call(this, editedBody);
            });
        } else {
            originalXhrSend.apply(this, arguments);
        }
    };

    // Intercept Fetch API
    const originalFetch = window.fetch;
    window.fetch = async function(resource, init) {
        if (typeof resource === 'string' && resource.includes(targetUrl)) {
            let body = init && init.body ? JSON.parse(init.body) : null;
            interceptAndEditRequest(init.method, resource, body, editedBody => {
                if (init) {
                    init.body = editedBody;
                }
                return originalFetch(resource, init);
            });
        } else {
            return originalFetch.apply(this, arguments);
        }
    };
})();


















incomi and outgoing 



// ==UserScript==
// @name         Targeted Network Logger
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Log request and response data for a specific API endpoint
// @match        https://www.tirangagames.top/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    const targetUrl = 'https://tirangaapi.com/api/webapi/GetNoaverageEmerdList';

    // Intercept XMLHttpRequest
    const originalXhrOpen = XMLHttpRequest.prototype.open;
    XMLHttpRequest.prototype.open = function(method, url, async, user, password) {
        this._url = url;
        this._method = method;
        this.addEventListener('readystatechange', function() {
            if (this.readyState === 4 && this._url.includes(targetUrl)) {
                console.log('Request to:', this._url);
                console.log('Method:', this._method);
                console.log('Response:', this.responseText);
            }
        });
        originalXhrOpen.apply(this, arguments);
    };

    const originalXhrSend = XMLHttpRequest.prototype.send;
    XMLHttpRequest.prototype.send = function(body) {
        if (this._url && this._url.includes(targetUrl)) {
            console.log('Request Body:', body);
        }
        originalXhrSend.apply(this, arguments);
    };

    // Intercept Fetch API
    const originalFetch = window.fetch;
    window.fetch = async function(resource, init) {
        if (typeof resource === 'string' && resource.includes(targetUrl)) {
            console.log('Fetch Request to:', resource);
            if (init) {
                console.log('Method:', init.method);
                console.log('Request Headers:', init.headers);
                console.log('Request Body:', init.body);
            }
            const response = await originalFetch.apply(this, arguments);
            const clonedResponse = response.clone();
            clonedResponse.text().then(body => {
                console.log('Fetch Response:', body);
            });
            return response;
        }
        return originalFetch.apply(this, arguments);
    };
})();