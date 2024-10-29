document.addEventListener('DOMContentLoaded', () => {
    const items = { ...localStorage };
    const isAuthed = items?.token;

    const wdgt = {
        idBox: 'wdgt',
        url_widget: 'https://next-starter.thirdweb-example.com/',
        url_style: 'http://localhost:8080/css/widget.css',

        init: function (identifier, byClass = false) {
            console.log("Begin Widget initialization");

            const observer = new MutationObserver((mutations, observer) => {
                let elements = [];
                if (byClass) {
                    elements = document.querySelectorAll(`.${identifier}`);
                    console.log(`Looking for elements by class: .${identifier}`);
                } else {
                    const element = document.getElementById(identifier || this.idBox);
                    if (element) {
                        elements.push(element);
                    }
                    console.log(`Looking for element by ID: #${identifier || this.idBox}`);
                }

                console.log(`Found elements:`, elements);

                if (elements.length > 0 && elements[0] != null) {
                    observer.disconnect(); // Stop observing once elements are found
                    try {
                        const XHR = ("onload" in new XMLHttpRequest()) ? XMLHttpRequest : XDomainRequest;
                        const xhr = new XHR();
                        xhr.open('GET', this.url_widget, true);

                        xhr.onload = function () {
                            if (this.status >= 200 && this.status < 300) {
                                elements.forEach(element => {
                                    element.innerHTML = this.responseText;
                                });
                            } else {
                                console.error('Failed to load widget content. Status:', this.status);
                            }
                        };

                        xhr.onerror = function () {
                            console.error('onerror', this.status);
                        };

                        xhr.send();
                    } catch (error) {
                        console.error('Error loading widget:', error);
                    }
                }
            });

            // Start observing the document body for changes
            observer.observe(document.body, { childList: true, subtree: true });

            // Initial check in case the elements are already present
            let elements = [];
            if (byClass) {
                elements = document.querySelectorAll(`.${identifier}`);
            } else {
                const element = document.getElementById(identifier || this.idBox);
                if (element) {
                    elements.push(element);
                }
            }

            if (elements.length > 0 && elements[0] != null) {
                observer.disconnect(); // Stop observing if elements are found initially
                try {
                    const XHR = ("onload" in new XMLHttpRequest()) ? XMLHttpRequest : XDomainRequest;
                    const xhr = new XHR();
                    xhr.open('GET', this.url_widget, true);

                    xhr.onload = function () {
                        if (this.status >= 200 && this.status < 300) {
                            elements.forEach(element => {
                                element.innerHTML = this.responseText;
                            });
                        } else {
                            console.error('Failed to load widget content. Status:', this.status);
                        }
                    };

                    xhr.onerror = function () {
                        console.error('onerror', this.status);
                    };

                    xhr.send();
                } catch (error) {
                    console.error('Error loading widget:', error);
                }
            }
        },

        addStyle: function () {
            const style = document.createElement('link');
            style.rel = 'stylesheet';
            style.type = 'text/css';
            style.href = this.url_style;
            document.head.appendChild(style);
        }
    };

    if (isAuthed) {
//        alert('You are authed');
    } else {
        // alert('You are not authed');
        // wdgt.init('root', false); // Change 'true' to 'false' if you want to use an ID instead of class
    }
});
