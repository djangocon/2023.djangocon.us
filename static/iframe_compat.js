$(function() {
  console.log('rendered', window.parent, window, window.parent !== window)
  if (window.parent !== window) {
    // We're in an iframe. Let's remove the navbar and the footer
    $('nav:not(.faq-nav),footer').remove()
    // With no navbar, the top padding for the content can be removed
    $('header.subpage-header').addClass('no-top')
  }
});
