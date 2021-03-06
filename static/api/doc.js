$(document).ready(function() {
    var sections = [];
    var offsets = {};
    var $li_a = $('#doc-menu ul li a');
    var $docMenu = $('#doc-menu');
    var $titleDiv = $('#title-div');
    var initialHeight = $docMenu.position().top;
    var widthRatio = $('#doc-all').width() / $(document).width();
    $li_a.each(function(i, e) {
        var targetId = this.getAttribute('href');
        var $target = $(targetId);
        var elY = $target.position().top;
        sections.push([elY, targetId, $(this.parentElement)]);
        offsets[targetId] = elY;
    });
    $li_a.click(function(e) {
        e.preventDefault();
        var targetId = this.getAttribute('href');
        window.scrollTo(0, offsets[targetId] + 90);
    })
    $(window).resize(function() {
        $docMenu.css({'width': widthRatio * $(document).width() / 4});
    })
    $(window).scroll(function() {
        var y = document.documentElement.scrollTop || document.body.scrollTop;

        var passedSections = sections.filter(function(a) { return a[0] <= y; });
        var currentSection = passedSections.length ? passedSections[passedSections.length - 1] : sections[0];

        sections.forEach(function(e, i) {
            if (currentSection == e) {
                e[2].addClass('active');
            } else {
                e[2].removeClass('active');
            }
        });

        if (y >= initialHeight + $titleDiv.height()) {
            $docMenu.css({'position': 'fixed', 'top': initialHeight + $titleDiv.height() / 2, 'left': $docMenu.position().left});
        } else {
            $docMenu.css({'position': 'static'});
        }
    });
    $(window).resize();
    $(window).scroll();
});