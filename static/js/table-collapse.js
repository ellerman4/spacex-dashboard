$(function() {
    /* Get total rows */
    var numRows = $('#past-launches-table').find('tr').length;

    /* get how many more can be shown */
    var getNumMore = function(c){var a=20,b=numRows-c;return b<a&&(a=b),a}

    /* how many items to show initially */
    var getInitialNumShown = function(){var a=9;return numRows<a&&(a=numRows),a}
    /* set how many are initially shown */
    var numShown = getInitialNumShown();

    /* set the numMore if less than 20 */
    var numMore = getNumMore(numShown);

    /* set more html */
    if (numMore > 0) {
        var more_html = '<p class="text-center"><button id="more">Show <span style="font-weight: bold;">' + numMore + '</span> More...</button></p>';
        $('#past-launches-table').find('tr:gt(' + (numShown - 1) + ')').hide().end().after(more_html);
    }
    $('#more').click(function() {
        /* determine how much more we should update */
        numMore = getNumMore(numShown);
        /* update num shown */
        numShown += numMore;
        $('#past-launches-table').find('tr:lt(' + numShown + ')').show();

        /* determine if to show more and how much left over */
        numMore = getNumMore(numShown);
    
        numMore>0?$("#more span").html(numMore):$("#more").remove()

    });
});