// Target external links blank
var all_links = document.querySelectorAll('a');
for (var i = 0; i < all_links.length; i++){
       var a = all_links[i];
       if(a.hostname != location.hostname && a.parentElement.id != 'download-button') {
            a.target = '_blank';
       }
}
