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
        $("#all_studies").DataTable({
            data: data,
            responsive: {
                details: {
                    type: 'column',
                    target: 'tr'
                }
            },
            columns: [
                { title: "Title", data: "title" },
                { title: "Year", data: "year" },
                { title: "Author", data: "first author" },
                { title: "Age", data: "age group" },
                { title: "AI Concepts", data: "concepts" },
                { title: "AI Practices", data: "practices" },
                { title: "AI Perspectives", data: "perspectives" },
                { title: "Assessment Type", data: "assessments"},
                { title: "Title", data: "title", visible:"false"  },
                { title: "Authors", data: "author", visible:"false" },
                { title: "Link", data: "url", visible:"false" },
            ],
            scrollY: 600,
            lengthMenu: [
                [10, 25, 50, -1],
                [10, 25, 50, 'All'],
            ],
            iDisplayLength: -1
        });
        
        // update data table style
        $( '#all_studies td' ).each(function() {
            $(this).css('max-width', '300px');
            $(this).css('overflow', 'hidden');
            $(this).css('text-overflow', 'ellipsis');
            $(this).css('white-space', 'nowrap');
        });
    });

    
    
     /*       .dataTable > td {
            }*/
});