/*!
* Start Bootstrap - Resume v7.0.5 (https://startbootstrap.com/theme/resume)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-resume/blob/master/LICENSE)
*/
//
// Scripts
//

window.addEventListener('DOMContentLoaded', event => {
    // Activate Bootstrap scrollspy on the main nav element
    const sideNav = document.body.querySelector('#sideNav');
    if (sideNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#sideNav',
            offset: 74,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

    // Have DataTable do it's thing
    $.getJSON('studies.json', function(data) {
        //console.log(data);
        $("#all_studies").DataTable({
            data: data,
            responsive: {
                details: {
                    type: 'column',
                    target: 'tr'
                }
            },
            columns: [
                { width: "300px", title: "Title", data: "Title" },
                { width: "60px", title: "Year", data: "Year" },
                { width: "60px", title: "Age", data: "Age Group" },
                { width: "200px", title: "Assessment Type", data: "Assessment Types" },
                { width: "200px", title: "AI Concepts", data: "Concepts" },
                { width: "200px", title: "AI Practices", data: "Practices" },
                { width: "200px", title: "AI Perspectives", data: "Perspectives" },
            ],
            scrollY: 600,
            lengthMenu: [
                [10, 25, 50, -1],
                [10, 25, 50, 'All'],
            ],
        });
    });
});