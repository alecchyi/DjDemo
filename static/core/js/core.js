/**********core.js**************/

YUI().use("node", function(Y) {

	var id_title = Y.one("#id_title");
	if (id_title != null) {
		id_title.on("focus", function(e) {
			id_title.addClass("focus_blog_title");
		});
		id_title.on("blur", function(e) {
			//    	id_title.removeClass("focus_blog_title");
		});
	}
});

var T = {};
T.tbwidget = {};
YUI(
		{
			modules : {
				'yahoo-dom-event' : {
					fullpath : 'http://a.tbcdn.cn/app/dp/eb/js/cubee/tbwidget/tblogin/yahoo-dom-event.js'
				},
				'tipInput' : {
					fullpath : 'http://a.tbcdn.cn/app/dp/eb/js/cubee/tbwidget/tipinput/tipinput.js',
					requires : [ 'yahoo-dom-event' ]
				}
			}
		}).use('tipInput', function(Y) {
	new T.tbwidget.tipInput("id_title");
});