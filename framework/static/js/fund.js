
//【控件初始化】    
  $("[id^='advanced_field']").hide(); //搜索模块：高级搜索控件默认隐藏；
  $("[id^='add_exist']").show(); //新增模块：默认显示“选择已有管理人”模块；
  $("[id^='add_new']").hide(); //新增模块：默认隐藏“新增管理人”模块；
  $("#xbrl_data1_history").show(); //新增模块：xbrl历史数据模块默认显示；
  $("#xbrl_data1_new").hide(); //新增模块：xbrl新数据模块默认隐藏；
  $("#xbrl_data2_history").hide(); //修改模块：xbrl历史数据模块默认隐藏；
  
  $("#search_manager").dropdown({
      apiSettings:    { url: '/stationconfig/manager/query/json/' },
      saveRemoteData: false,
  }); //搜索模块：管理人下拉框AJax加载；

  $("#search_fund").dropdown({
      apiSettings: { url: '/stationconfig/fund/query/json/' },
  }); //搜索模块：项目名称下拉框AJax加载；

  $("#add_manager_exist").dropdown({
      apiSettings: { url: "{% url 'stationconfig:query_json_manager' %}" },
      saveRemoteData:false,
  }); //新增模块：选择管理人下拉框AJax加载；
  
  $("#modify_manager").dropdown({
      apiSettings: { url: "{% url 'stationconfig:query_json_manager' %}" },
      saveRemoteData:false,
  }); //修改模块：选择管理人下拉框AJax加载；
      
  $("#add_fundtype").dropdown(); //新增模块：选择项目类型下拉框；
  $("#add_history").dropdown(); //新增模块：选择是否历史数据下拉框；
  $("#modify_fundtype").dropdown(); //修改模块：选择项目类型下拉框；
  $("#modify_history").dropdown(); //修改模块：选择是否历史数据下拉框；
       
  $(".ui.modal").modal({ 
      detachable:     true,
      autofocus:      false,
      observeChanges:   false,    
      allowMultiple:    false,
      keyboardShortcuts:  false,
      context:      "body",
      closable:     false,
      transition:     "scale",
      duration:     400, 
      inverted:       true,
      blurring:       false
  }); //所有模态框初始化；
  $("#add_modal").modal("hide"); //新增模态框默认隐藏；
  $("#modify_modal").modal("hide"); //修改模态框默认隐藏；
  $("#delete_modal").modal("hide"); //删除模态框默认隐藏；
  
//【函数定义】
  function copyManager(){
      document.all["add_pathfrom_new2"].value=document.all["add_manager_new"].value;
      document.all["add_pathto_temp_new1"].value=document.all["add_manager_new"].value;
      document.all["add_move_new1"].value=document.all["add_manager_new"].value;
      document.all["add_pathto_new1"].value=document.all["add_manager_new"].value;

      document.all["add_md_new1"].value=document.all["add_manager_new"].value;
      document.all["add_mput_new1"].value=document.all["add_manager_new"].value;
      document.all["add_send_new2"].value=document.all["add_manager_new"].value;

      document.all["add_if_exist_new1"].value=document.all["add_manager_new"].value;
      document.all["add_move_file_new1"].value=document.all["add_manager_new"].value;
    } //新增模块：新增管理人时同步管理人输入框；

    function copyManagerCode(){
      document.all["add_pathfrom_new1"].value=document.all["add_manager_code_new"].value;
      document.all["add_send_new1"].value=document.all["add_manager_code_new"].value;
    } //新增模块：新增管理人时同步管理人代码输入框；

    function copyFund(){
      document.all["add_pathto_temp_new2"].value=document.all["add_fundname"].value;
      document.all["add_move_new2"].value=document.all["add_fundname"].value;
      document.all["add_pathto_new2"].value=document.all["add_fundname"].value;

      document.all["add_md_new2"].value=document.all["add_fundname"].value;
      document.all["add_mput_new2"].value=document.all["add_fundname"].value;
      document.all["add_if_exist_new2"].value=document.all["add_fundname"].value;
      document.all["add_move_file_new2"].value=document.all["add_fundname"].value;
    } //新增模块：同步项目名称输入框；

    function copyFundCode(){
      document.all["add_move_new3"].value=document.all["add_fundcode"].value;
    } //新增模块：同步项目代码输入框；
    
//【事件】
    $('#advanced_find').on('click', function(){
      $("[id^='advanced_field']").toggle();
    }); //搜索模块：点击高级搜索按钮展示高级搜索控件；
    
    $('#manage_add').on('click', function(){
	    $("#add_modal").modal("show");
    }); //新增模块：点击新增按钮显示新增模态框；

    $('#add_close').on('click', function(){
      $("#add_modal").modal("hide");
    }); //新增模块：点击新增模态框中的取消按钮关闭新增模态框；
    
    $('#exist_or_add').on('click', function(){
      $("[id^='add_exist']").toggle();
      $("[id^='add_new']").toggle();
      $("#add_manager_code_exist").attr({"value" : ''});
      $("#add_pathfrom_new2").attr({"value" : ''});
      $("#add_pathto_temp_new1").attr({"value" : ''});
      $("#add_move_new1").attr({"value" : ''});
      $("#add_pathto_new1").attr({"value" : ''});
      $("#add_md_new1").attr({"value" : ''});
      $("#add_mput_new1").attr({"value" : ''});
      $("#add_send_new2").attr({"value" : ''});
      $("#add_if_exist_new1").attr({"value" : ''});
      $("#add_move_file_new1").attr({"value" : ''});
      $("#add_pathfrom_new1").attr({"value" : ''});
      $("#add_send_new1").attr({"value" : ''});

      if ($('#exist_or_add').text()=='新增管理人'){
        $('#exist_or_add').text('选择已有管理人');
        $("#add_manager_new").val('');
        $("#add_manager_code_new").val('');
      }
      else {
        $('#exist_or_add').text('新增管理人');
        $("#add_manager_exist").dropdown('clear');
      }
    }); //新增模块：输入管理人时切换“已有管理人”和“新增管理人”；
    
 
    $('.modify').on('click', function(){ 	    
 	    var manager_id = $(this).parents("tr").find(".manager").attr("id");
      var manager = $(this).parents("tr").find(".manager").text();
 	    var manager_code = $(this).parents("tr").find(".manager_code").text();
 	    var fundname = $(this).parents("tr").find(".fundname").text();
 	    var fundid = $(this).parents("tr").find(".fundname").attr("id");
 	    var fundcode = $(this).parents("tr").find(".fundcode").text();
 	    var fundtype = $(this).parents("tr").find(".fundtype").text();
      var history =$(this).parents("tr").find(".history").text();
    	var pathfrom = $(this).parents("tr").find(".pathfrom").text();
    	var pathto_temp = $(this).parents("tr").find(".pathto_temp").text();
    	var move = $(this).parents("tr").find(".move").text();
    	var pathto = $(this).parents("tr").find(".pathto").text();
    	var md = $(this).parents("tr").find(".md").text();
    	var mput = $(this).parents("tr").find(".mput").text();
    	var send = $(this).parents("tr").find(".send").text();
    	var if_exist = $(this).parents("tr").find(".if_exist").text();
    	var move_file = $(this).parents("tr").find(".move_file").text(); //修改模块：获取当前行的所有数据；
    
   	  $("#modify_fund").attr({"value" : fundname});
   	  $("#modify_fundid").attr({"value" : fundid});
   	  $("#modify_fundcode").attr({"value" : fundcode});
   	 $("#modify_pathfrom").attr({"value" : pathfrom});
     $("#modify_pathto_temp").attr({"value" : pathto_temp});
     $("#modify_move").attr({"value" : move});
     $("#modify_pathto").attr({"value" : pathto});
     $("#modify_md").attr({"value" : md});
     $("#modify_mput").attr({"value" : mput});
     $("#modify_send").attr({"value" : send});
     $("#modify_if_exist").attr({"value" : if_exist});
     $("#modify_move_file").attr({"value" : move_file}); //修改模块：重置输入框的默认值；
   	  
      $("#modify_manager").dropdown('set text', manager);
      $("#modify_manager").dropdown('set value', manager_id);
      $("#modify_fundtype").dropdown('set text', fundtype);
      $("#modify_fundtype").dropdown('set value', fundtype); 
      $("#modify_history").dropdown('set text', history);
      $("#modify_history").dropdown('set value', history); //修改模块：重置下拉框的默认选项；
      
      if (fundtype=='xbrl'){
        $("#xbrl_data2_history").show();} //修改模块：项目类型是xbrl时显示xbrl部分控件；
      
        $("#modify_modal").modal("show"); //修改模块：点击修改按钮显示修改模态框；
      }); 
      
    $('#modify_close').on('click', function(){
      $("#modify_modal").modal("hide");
    }); //修改模块：点击修改模态框中的取消按钮关闭修改模态框；
    
    
    $('.delete').on('click', function(){
      var fundid = $(this).parents("tr").find(".fundname").attr("id");
  	  var manager = $(this).parents("tr").find(".manager").text(); 
      var manager_code = $(this).parents("tr").find(".manager_code").text(); 
  	  var fundname = $(this).parents("tr").find(".fundname").text();
      var fundtype = $(this).parents("tr").find(".fundtype").text(); //删除模块：获取当前行的所有数据；
 
      $("#delete_fundid").attr({"value" : fundid});
      document.getElementById("delete_manager").innerHTML = manager;
      document.getElementById("delete_manager_code").innerHTML = manager_code;
      document.getElementById("delete_fundname").innerHTML = fundname;
      document.getElementById("delete_fundtype").innerHTML = fundtype; //删除模块：显示获取的数据；
      $("#delete_modal").modal("show"); //删除模块：点击删除按钮显示删除模态框；
    }); 
     
    $('#delete_close').on('click', function(){
      $("#delete_modal").modal("hide");
    }); //删除模块：点击删除模态框中的取消按钮关闭删除模态框；
    
    
    $("#search_manager").dropdown({
        onChange:       function(value, text){alert(value);
        $("#search_fund").dropdown({
        apiSettings: {
            url: '/stationconfig/fund/query/json/'+value },
    });},
    }); //搜索模块：管理人和项目名称下拉框联动；

    $("#add_manager_exist").dropdown({
        onChange:function(value, text, $choice){ 
          var id = $('#add_manager_exist').dropdown('get value');
          $.ajaxSetup({ data: {csrfmiddlewaretoken: '{{ csrf_token }}' },   });
          $.ajax({    
            type:'post',        
            url:"{% url 'stationconfig:select_manager' %}",    
            data:{'manager_id':id},   
            cache:false,    
            dataType:'json',    
            success:function(data,textStatus,jqXHR){alert(data.manager_code+text);
              $("#add_manager_code_exist").attr({"value" : data.manager_code});
              $("#add_pathfrom_new2").attr({"value" : text});
              $("#add_pathto_temp_new1").attr({"value" : text});
              $("#add_move_new1").attr({"value" : text});
              $("#add_pathto_new1").attr({"value" : text});
              $("#add_md_new1").attr({"value" : text});
              $("#add_mput_new1").attr({"value" : text});
              $("#add_send_new2").attr({"value" : text});
              $("#add_if_exist_new1").attr({"value" : text});
              $("#add_move_file_new1").attr({"value" : text});
              $("#add_pathfrom_new1").attr({"value" : data.manager_code});
              $("#add_send_new1").attr({"value" : data.manager_code});
            },
          });
        },
      }); //新增模块：选择已有管理人和其管理人代码联动
 
    $("#add_fundtype").dropdown({
        onChange:function(value, text){ 
          var history11 = $('#add_history').dropdown('get value');
          alert(history11);
          if (value=='xbrl'){
            if (history=='True'){
              $("#xbrl_data1_history").show();
              $("#xbrl_data1_new").hide();
            }
            if (history=='False'){
              $("#xbrl_data1_history").hide();
              $("#xbrl_data1_new").show();
            }
          }
          if (value=='ta'){
            $("#xbrl_data1_history").hide();
            $("#xbrl_data1_new").hide();
          }
        },
    }); //新增模块：项目类型控制对应的详细内容输入框；

    $("#add_history").dropdown({
      onChange:function(value, text){ 
        var fundtype = $('#add_fundtype').dropdown('get value');
          alert(fundtype);
        if (value=='True' && fundtype=='xbrl'){
          $("#xbrl_data1_history").show();
          $("#xbrl_data1_new").hide();
        }
        if (value=='False' && fundtype=='xbrl'){
          $("#xbrl_data1_history").hide();
          $("#xbrl_data1_new").show();
        }
      }
    }); //新增模块：xbrl类型添加非历史项目时根据模板自动生成；

    $("#modify_manager").dropdown({
        onChange:function(value, text, $choice){ 
          var id = $('#modify_manager').dropdown('get value');
          $.ajaxSetup({ data: {csrfmiddlewaretoken: '{{ csrf_token }}' },   });
          $.ajax({    
            type:'post',        
            url:"{% url 'stationconfig:select_manager' %}",    
            data:{'manager_id':id},   
            cache:false,    
            dataType:'json',    
            success:function(data,textStatus,jqXHR){
              $("#modify_manager_code").attr({"value" : data.manager_code});},
          });
        },
      }); //修改模块：修改管理人后显示对应管理人代码；
    
    $("#modify_fundtype").dropdown({
        onChange:function(value){ 
          if (value=='xbrl'){$("#xbrl_data2_history").show();}
          if (value=='ta'){$("#xbrl_data2_history").hide();}
        },
      });