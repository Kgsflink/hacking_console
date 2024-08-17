// ==UserScript==
// @name         Intercept, Filter, and Download Requests
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  Intercept, filter, and download payload data from requests
// @author       Your Name
// @match        https://*.tirangaapi.com/*
// @grant        none
// @run-at       document-start
// ==/UserScript==

(function() {
    'use strict';

    let interceptEnabled = true; // Automatically enable interception
    let allData = []; // Array to store data from all pages
    let targetCount = parseInt(prompt("Enter the number of data entries you want to collect:"), 10);

    console.log('Request interception is set up and enabled');
    console.log(`Target data count is set to ${targetCount} entries.`);

    // Function to handle and log fetch request and response
    const handleFetch = (response, args) => {
        if (interceptEnabled && (response.url.includes("tirangaapi.com/api/webapi/GetGameIssue") || response.url.includes("tirangaapi.com/api/webapi/GetNoaverageEmerdList"))) {
            console.log('Intercepted fetch request to:', response.url);
            console.log('Request headers:', args[1]?.headers);
            console.log('Request payload:', args[1]?.body);
            response.clone().json().then(data => {
                console.log('Response payload:', data);
                if (data.code === 0 && data.data && data.data.list) {
                    allData = allData.concat(data.data.list); // Collect the data
                    console.log('Collected data so far:', allData.length, 'entries');

                    if (allData.length >= targetCount) {
                        // Save data when targetCount entries are collected
                        downloadData(allData);
                        allData = []; // Reset data after saving
                    }

                    if (data.data.pageNo === data.data.totalPage) {
                        // Process the remaining data if any
                        processData(allData);
                    }
                }
            }).catch(err => {
                console.error('Error reading response:', err);
            });
        }
    };

    // Function to trigger file download
    const downloadData = (data) => {
        const blob = new Blob([JSON.stringify(data)], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `collected_data_${Date.now()}.json`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
        console.log('Data download initiated.');
    };

    // Override the native fetch function
    const originalFetch = window.fetch;
    window.fetch = function(...args) {
        return originalFetch(...args).then(response => {
            handleFetch(response, args);
            return response;
        }).catch(err => {
            console.error('Fetch error:', err);
            throw err;
        });
    };

    // Override the native XMLHttpRequest
    const originalXhrOpen = XMLHttpRequest.prototype.open;
    XMLHttpRequest.prototype.open = function(method, url, ...rest) {
        this._url = url;  // Store the URL for use in the send method
        return originalXhrOpen.call(this, method, url, ...rest);
    };

    const originalXhrSend = XMLHttpRequest.prototype.send;
    XMLHttpRequest.prototype.send = function(body) {
        this.addEventListener('load', function() {
            if (interceptEnabled && (this._url.includes("tirangaapi.com/api/webapi/GetGameIssue") || this._url.includes("tirangaapi.com/api/webapi/GetNoaverageEmerdList"))) {
                console.log('Intercepted XHR request to:', this._url);
                console.log('Request payload:', body);
                try {
                    const responseJson = JSON.parse(this.responseText);
                    console.log('Response payload:', responseJson);
                    if (responseJson.code === 0 && responseJson.data && responseJson.data.list) {
                        allData = allData.concat(responseJson.data.list); // Collect the data
                        console.log('Collected data so far:', allData.length, 'entries');

                        if (allData.length >= targetCount) {
                            // Save data when targetCount entries are collected
                            downloadData(allData);
                            allData = []; // Reset data after saving
                        }

                        if (responseJson.data.pageNo === responseJson.data.totalPage) {
                            // Process the remaining data if any
                            processData(allData);
                        }
                    }
                } catch (err) {
                    console.error('Error parsing response JSON:', err);
                    console.log('Response payload:', this.responseText);
                }
            }
        });
        return originalXhrSend.call(this, body);
    };

    // Function to process the remaining collected data
    const processData = (data) => {
        if (data.length > 0) {
            downloadData(data);
        }
        console.log('Final collected data:', data.length, 'entries');
    };

})();
















for next click




// Function to extract data from the current page
function extractData() {
    const latestResults = [];
    const vanRows = document.querySelectorAll('.GameRecord__C-body .van-row');

    vanRows.forEach(row => {
        const cols = row.querySelectorAll('.van-col');
        if (cols.length >= 4) {
            const round = cols[0].textContent.trim();
            const numElement = cols[1].querySelector('.GameRecord__C-body-num');
            const num = numElement ? numElement.textContent.trim() : '';
            const size = cols[2].textContent.trim();
            const originDivs = cols[3].querySelectorAll('.GameRecord__C-origin-I');
            const origins = Array.from(originDivs).map(div => div.className.split(' ')[1]);
            latestResults.push({ round, num, size, origins });
        }
    });
    
    return latestResults;
}

// Function to navigate to the next page
function clickNext() {
    const nextButton = document.querySelector('.GameRecord__C-foot-next .GameRecord__C-icon');
    if (nextButton) {
        nextButton.click();
    } else {
        console.log("No more pages to navigate.");
    }
}

// Function to handle the extraction process for the specified number of pages
async function extractDataForRounds() {
    const roundsToExtract = parseInt(prompt("Enter the number of rounds to extract:"), 10);
    if (isNaN(roundsToExtract) || roundsToExtract <= 0) {
        console.error("Invalid number of rounds.");
        return;
    }

    let allResults = [];
    for (let round = 0; round < roundsToExtract; round++) {
        // Wait for the page to load before extracting data
        await new Promise(resolve => setTimeout(resolve, 10)); // Adjust the delay as needed
        const pageData = extractData();
        allResults = allResults.concat(pageData);
        clickNext();
    }

    console.log(allResults);
}

// Extract data for the specified number of rounds
extractDataForRounds();





















