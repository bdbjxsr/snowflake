
//datatable page semantic datatable settings
(function (window, document, undefined) {
    var factory = function ($, DataTable) {
        "use strict";

        /* Set the defaults for DataTables initialisation */
        $.extend(true, DataTable.defaults, {
            dom:
                "<'left aligned eight wide column'l><'right aligned eight wide column'f>" +
                "<'sixteen wide column'tr>" +
                "<'left aligned four wide column'i><'right aligned twelve wide column'p>",
            renderer: 'semantic'
        });

        $.extend(DataTable.ext.pager, {
            full_numbers_icon: DataTable.ext.pager.full_numbers
        });

        /* Default class modification */
        $.extend(DataTable.ext.classes, {
            sWrapper: "ui grid dataTables_wrapper ",
            sFilterInput: "",
            sLengthSelect: ""
        });

        /* Bootstrap paging button renderer */
        DataTable.ext.renderer.pageButton.semantic = function (settings, host, idx, buttons, page, pages) {
            var api = new DataTable.Api(settings);
            var classes = settings.oClasses;
            var lang = settings.oLanguage.oPaginate;
            var btnDisplay, btnClass, btnIcon, counter = 0;
            var addIcons = ((!api.init().pagingType ? '' : api.init().pagingType.toLowerCase()).indexOf('icon') !== -1);

            var attach = function (container, buttons) {
                var i, ien, node, button;
                var clickHandler = function (e) {
                    e.preventDefault();
                    if (!$(e.currentTarget).hasClass('disabled')) {
                        api.page(e.data.action).draw('page');
                    }
                };

                for (i = 0, ien = buttons.length ; i < ien ; i++) {
                    button = buttons[i];

                    if ($.isArray(button)) {
                        attach(container, button);
                    }
                    else {
                        btnDisplay = '';
                        btnClass = '';
                        btnIcon = '';
                        switch (button) {
                            case 'ellipsis':
                                btnDisplay = (addIcons ? '<i class="mini ellipsis horizontal icon"></i>' : '&hellip;');
                                btnClass = 'disabled';
                                break;

                            case 'first':
                                btnIcon = (addIcons ? '<i class="angle single left icon"></i>' : '');
                                btnDisplay = btnIcon + lang.sFirst;
                                btnClass = button + (page > 0 ?
                                    '' : ' disabled');
                                break;

                            case 'previous':
                                btnIcon = (addIcons ? '<i class="angle double left icon"></i>' : '');
                                btnDisplay = btnIcon + lang.sPrevious;
                                btnClass = button + (page > 0 ?
                                    '' : ' disabled');
                                break;

                            case 'next':
                                btnIcon = (addIcons ? '<i class="angle double right icon"></i>' : '');
                                btnDisplay = lang.sNext + btnIcon;
                                btnClass = button + (page < pages - 1 ?
                                    '' : ' disabled');
                                break;

                            case 'last':
                                btnIcon = (addIcons ? '<i class="angle single right icon"></i>' : '');
                                btnDisplay = lang.sLast + btnIcon;
                                btnClass = button + (page < pages - 1 ?
                                    '' : ' disabled');
                                break;

                            default:
                                btnDisplay = button + 1;
                                btnClass = page === button ?
                                    'active' : '';
                                break;
                        }

                        if (btnDisplay) {
                            node = $('<a>', {
                                'class': classes.sPageButton + ' ' + btnClass + ' item ',
                                'id': idx === 0 && typeof button === 'string' ?
                                    settings.sTableId + '_' + button :
                                    null
                            }).html(btnDisplay).appendTo(container);

                            settings.oApi._fnBindAction(
                                node, { action: button }, clickHandler
                            );

                            counter++;
                        }
                    }
                }
            };

            // IE9 throws an 'unknown error' if document.activeElement is used
            // inside an iframe or frame.
            var activeEl;

            try {
                // Because this approach is destroying and recreating the paging
                // elements, focus is lost on the select button which is bad for
                // accessibility. So we want to restore focus once the draw has
                // completed
                activeEl = $(host).find(document.activeElement).data('dt-idx');
            }
            catch (e) { }

            attach(
                $(host).empty().html('<div class="ui stackable small pagination menu" />').children('div'),
                buttons
            );

            if (activeEl) {
                $(host).find('[data-dt-idx=' + activeEl + ']').focus();
            }
        };
    }; // /factory

    // Define as an AMD module if possible
    if (typeof define === 'function' && define.amd) {
        define(['jquery', 'datatables'], factory);
    }
    else if (typeof exports === 'object') {
        // Node/CommonJS
        factory(require('jquery'), require('datatables'));
    }
    else if (jQuery) {
        // Otherwise simply initialise as normal, stopping multiple evaluation
        factory(jQuery, jQuery.fn.dataTable);
    }
})(window, document);

$(document).ready(function () {
    var dtable = $('#data_table').DataTable({
        pagingType: "full_numbers",
        order: [0, 'asc'],
        lengthMenu: [[5, 10, -1], [5, 10, "全部"]],
        filter: false,
        responsive: true,
        buttons: [
            {
                extend: 'csv',
                text: 'Copy all data',
                exportOptions: {
                    modifier: {
                        search: 'none'
                    }
                }
            }
        ],
        columnDefs: [
            {
              "targets": [ 5 ],
              "visible": false
            }
        ],
        language: {
        	        "sProcessing": "处理中...",
        	        "sLengthMenu": "显示 _MENU_ 项结果",
        	        "sZeroRecords": "没有匹配结果",
        	        "sInfo": "显示第 _START_ 至 _END_ 项结果，共 _TOTAL_ 项",
        	        "sInfoEmpty": "显示第 0 至 0 项结果，共 0 项",
        	        "sInfoFiltered": "(由 _MAX_ 项结果过滤)",
        	        "sInfoPostFix": "",
        	        "sSearch": "搜索:",
        	        "sUrl": "",
        	        "sEmptyTable": "表中数据为空",
        	        "sLoadingRecords": "载入中...",
        	        "sInfoThousands": ",",
        	        "oPaginate": {
        	            "sFirst": "首页",
        	            "sPrevious": "上页",
        	            "sNext": "下页",
        	            "sLast": "末页"
        	        },
        	        "oAria": {
        	            "sSortAscending": ": 以升序排列此列",
        	            "sSortDescending": ": 以降序排列此列"
        	        }
        	    }
    });
    $('#user_manage_operate').on( 'click', function (e) {
        e.preventDefault();
 
        // Get the column API object
        var column = dtable.column( $(this).attr('data-column') );
 
        // Toggle the visibility
        column.visible( ! column.visible() );
    } );
    
});

