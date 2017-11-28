 /**
  * 增加标签页
  */
 function addTab(options) {			
     //option:
     //tabMainName:tab标签页所在的容器
     //tabContentMainName:tab标签页的内容所在容器
     //tabName:当前tab的名称
     //tabTitle:当前tab的标题
     //tabUrl:当前tab所指向的URL地址
     var exists = checkTabIsExists(options.tabMainName, options.tabName);
     if(exists){
         $("#tab_a_"+options.tabName).click();
     } else {
         $("#"+options.tabMainName).append('<li id="tab_li_'+options.tabName+'"><a href="#tab_content_'+options.tabName+'" data-toggle="tab" id="tab_a_'+options.tabName+'">'+options.tabTitle+'&nbsp<i class="fa fa-remove tab-close" onclick="closeTab(this);"></i></a></li>');
         var content = '';
         if(options.content){
             content = option.content;
         } else {
             content = '<iframe src="' + options.tabUrl + '" width="100%" frameborder="no" border="0" marginwidth="0" onload="setIframeHeight(this)"></iframe>';
         }
         $("#"+options.tabContentMainName).append('<div id="tab_content_'+options.tabName+'" role="tabpanel" class="tab-pane" id="'+options.tabName+'">'+content+'</div>');
         $("#tab_a_"+options.tabName).click();
     }
 };
 /**
  * 关闭标签页
  * @param button
  */
function closeTab (button) {    
	var li_id = $(button).parent().parent().attr('id');
	var id = li_id.replace("tab_li_","");
	 
	//如果关闭的是当前激活的TAB，激活他的前一个TAB
	if ($("li.active").attr('id') == li_id) {
	    $("li.active").prev().find("a").click();
			}
 
			//关闭TAB
	$("#" + li_id).remove();
	$("#tab_content_" + id).remove();
		};
 
		/**
 * 判断是否存在指定的标签页
 * @param tabMainName
 * @param tabName
 * @returns {Boolean}
 */
function checkTabIsExists(tabMainName, tabName){
    var tab = $("#"+tabMainName+" > #tab_li_"+tabName);
    //console.log(tab.length)
    return tab.length > 0;
}
$('.navbar-brand').on('click', function(ev) {
	var options={
		tabMainName:"tab-title-id",
		tabContentMainName:"page-wrapper",
		tabName:"home",
		tabTitle:"主页",
		tabUrl:"#"
	};
	addTab(options);
});
$('#side-menu-dashbord').on('click', function(ev) {
	var options={
		tabMainName:"tab-title-id",
		tabContentMainName:"page-wrapper",
		tabName:"side-menu-dashbord",
		tabTitle:"百度",
		tabUrl:"https://www.baidu.com"
	};
	addTab(options);
});
$('#side-menu-permission').on('click', function(ev) {
	var options={
		tabMainName:"tab-title-id",
		tabContentMainName:"page-wrapper",
		tabName:"side-menu-permission",
		tabTitle:"权限控制",
		tabUrl:"{% url 'polls:permission' %}"
	};
	addTab(options);
});