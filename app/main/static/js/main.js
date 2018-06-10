$('#myModal').modal({
    backdrop: 'static',
    keyboard: false
});

$('#myTabs a').click(function (e) {
    e.preventDefault()
    $(this).tab('show')
});


function confirm() {
    var number = $("#number").val();
    var pwd1 = $("#exampleInputPassword1").val();
    var pwd2 = $("#exampleInputPassword2").val();
    //var pwd1 = document.getElementById('exampleInputPassword1').value;
    //var pwd2 = document.getElementById('exampleInputPassword2').value;
    //if(number.toString().length != 11) {
    //  $.message({
    //    message: '用户名格式错误',
    //  type: 'warning'
    //});
    //}
    //else
    if (number == "" || pwd1 == "") {
        //alert("用户名或密码不能为空");
        $.message({
            message: '用户名或密码不能为空',
            type: 'warning'
        });
    } else if (pwd1 != pwd2) {
        //alert("密码不一致");
        $.message({
            message: '密码不一致',
            type: 'warning'
        });
    } else {
        //ajax 请求
        var data = {
            "user": number,
            "passwd": pwd1
        };
        $.ajax({
            url: '/register/',
            type: 'POST',
            data: JSON.stringify(data),
            contentType: 'application/json; charset=UTF-8',
            dataType: 'json',
            success: function (msg) {
                //alert(msg);
                if (msg.ret == true) {
                    $.message({
                        message: '注册成功',
                        type: 'success'
                    });
                    self.location = '/login';
                } else {
                    $.message({
                        message: '注册失败',
                        type: 'error'
                    });
                }
            },
            error: function (jqXHR, textStatus, errorThrown) {
                /*错误信息处理*/
                //alert("未知错误");
                $.message({
                    message: '未知错误',
                    type: 'error'
                });
            }
        });
    }
};


$('#login').on('click', function () {
    var number = $('#login_number').val();
    var passwd = $('#login_password').val();
    if (number == "" || passwd == "") {
        $.message({
            message: '学号或密码为空',
            type: 'warning'
        });
    } else {
        //ajax 请求
        var data = {
            "user": number,
            "passwd": passwd
        };
        $.ajax({
            url: '/login/',
            type: 'POST',
            data: JSON.stringify(data),
            contentType: 'application/json; charset=UTF-8',
            dataType: 'json',
            success: function (msg) {
                //alert(msg);
                if (msg.ret == true) {
                    $.message({
                        message: '登录成功',
                        type: 'success'
                    });
                    self.location = '/';
                } else {
                    $.message({
                        message: '用户名或密码错误',
                        type: 'warning'
                    });
                }
            },
            error: function (jqXHR, textStatus, errorThrown) {
                /*错误信息处理*/
                //alert("未知错误");
                $.message({
                    message: '未知错误',
                    type: 'error'
                });
            }
        });
    }
});

$('#choice').on('click', function () {
    var value = $('input:radio:checked').val();
    //alert(value);
    if (value == null) {
        $.message({
            message: '没有选择座位',
            type: 'warning'
        });
    } else {
        var data = {
            "table_id": value
        };
        var span_id = "span" + value;
        var text = $('#' + span_id).text();
        //alert(span_id);
        //alert(text);
        if (text == '暂离') {
            $('#myModal5').modal('show');
            $.ajax({
                url: '/leave_info/',
                type: 'POST',
                data: JSON.stringify(data),
                contentType: 'application/json; charset=UTF-8',
                dataType: 'json',
                success: function (msg) {
                    //alert(msg);
                    if (msg.ret == "") {
                        //$('#info1').text('空');
                        //$('#info2').text('无');
                        //$('#info3').text('未选择座位');
                    } else {
                        //alert(msg.ret[2]);
                        var seat = msg.ret[0];
                        var time = msg.ret[3];
                        //alert(seat);
                        if (seat <= 10) {
                            $('#temp_info1').text('1楼' + seat + '座位');
                        } else if (seat <= 20) {
                            $('#temp_info1').text('2楼' + seat + '座位');
                        } else if (seat <= 30) {
                            $('#temp_info1').text('3楼' + seat + '座位');
                        } else {
                            $('#temp_info1').text('4楼' + seat + '座位');
                        }

                        $('#temp_info2').text(time);

                        $('#temp_info3').text(msg.ret[2] + '小时');


                    }
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    /*错误信息处理*/
                    //alert("未知错误");
                    $.message({
                        message: '未知错误',
                        type: 'error'
                    });
                }
            });
        } else {

            $.ajax({
                url: '/',
                type: 'POST',
                data: JSON.stringify(data),
                contentType: 'application/json; charset=UTF-8',
                dataType: 'json',
                success: function (msg) {
                    //alert(msg);
                    if (msg.ret == true) {
                        $.message({
                            message: '选座成功',
                            type: 'success'
                        });
                        self.location = '/';
                    } else if (msg.ret == '已闭馆') {
                        $.message({
                            message: '已闭馆',
                            type: 'warning'
                        });
                    } else {
                        $.message({
                            message: '你已选过或已有人',
                            type: 'warning'
                        });
                    }
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    /*错误信息处理*/
                    $.message({
                        message: '未知错误',
                        type: 'error'
                    });
                }
            });
        }

    }
});

$('#leave').on('click', function () {
    //ajax 请求
    $.ajax({
        url: '/leave/',
        type: 'GET',
        //data: JSON.stringify(data),
        contentType: 'application/json; charset=UTF-8',
        dataType: 'json',
        success: function (msg) {
            //alert(msg);
            if (msg.ret == true) {
                $.message({
                    message: '你已离开',
                    type: 'info'
                });
                self.location = '/';
            } else {
                $.message({
                    message: '你还没有座位',
                    type: 'warning'
                });
            }
        },
        error: function (jqXHR, textStatus, errorThrown) {
            /*错误信息处理*/
            //alert("未知错误");
            $.message({
                message: '未知错误',
                type: 'error'
            });
        }
    });
});

$('#info').on('click', function () {
    //ajax 请求
    $.ajax({
        url: '/info/',
        type: 'GET',
        //data: JSON.stringify(data),
        contentType: 'application/json; charset=UTF-8',
        dataType: 'json',
        success: function (msg) {
            //alert(msg);
            if (msg.ret == "") {
                $('#info1').text('空');
                $('#info2').text('无');
                $('#info3').text('未选择座位');
            } else {
                //alert(msg.ret[2]);
                var seat = msg.ret[0];
                var time = msg.ret[3];
                //alert(seat);
                var s = seat % 10;
                if (s == 0) {
                    s = 10;
                }
                if (seat <= 10) {
                    $('#info1').text('1楼' + s + '座位');
                } else if (seat <= 20) {
                    $('#info1').text('2楼' + s + '座位');
                } else if (seat <= 30) {
                    $('#info1').text('3楼' + s + '座位');
                } else {
                    $('#info1').text('4楼' + s + '座位');
                }

                $('#info2').text(time);
                if (msg.ret[2] == 0) {
                    $('#info3').text("有人");
                } else {
                    $('#info3').text("暂离");
                    $('#tmp_leave_time').remove();
                    $('#append_info').append("<laber id='tmp_leave_time'>暂离时间:<laber id='info4'></laber></laber>");
                    $('#info4').text(msg.ret[2] + '小时');
                }

            }
        },
        error: function (jqXHR, textStatus, errorThrown) {
            /*错误信息处理*/
            //alert("未知错误");
            $.message({
                message: '未知错误',
                type: 'error'
            });
        }
    });
});

$('#temp_leave').on('click', function () {
    //ajax 请求
    var leave_time = $('#leave_time').val();
    // alert(leave_time);
    if (leave_time == "" || isNaN(leave_time)) {
        $.message({
            message: '离开时间格式错误',
            type: 'warning'
        });
    } else if (leave_time > 2) {
        $.message({
            message: '离开时间不能太长',
            type: 'warning'
        });
    } else {
        var data = {
            "leave_time": leave_time
        };
        $.ajax({
            url: '/temporary_leave/',
            type: 'POST',
            data: JSON.stringify(data),
            contentType: 'application/json; charset=UTF-8',
            dataType: 'json',
            success: function (msg) {
                //alert(msg);
                if (msg.ret == true) {
                    $.message({
                        message: '你已暂离',
                        type: 'info'
                    });
                    self.location = '/';
                } else {
                    $.message({
                        message: '无法暂离',
                        type: 'warning'
                    });
                }
            },
            error: function (jqXHR, textStatus, errorThrown) {
                /*错误信息处理*/
                //alert("未知错误");
                $.message({
                    message: '未知错误',
                    type: 'error'
                });
            }
        });
    }

});

$('#suggest').on('click', function () {
    //ajax 请求
    var text = $('#txt').val();
    var contact = $('#contact').val();
    if (text == "") {
        $.message({
            message: '反馈内容不能为空',
            type: 'error'
        });
    } else {
        var data = {
            "text": text,
            "contact": contact
        };
        $.ajax({
            url: '/suggest/',
            type: 'POST',
            data: JSON.stringify(data),
            contentType: 'application/json; charset=UTF-8',
            dataType: 'json',
            success: function (msg) {
                //alert(msg);
                if (msg.ret == true) {
                    $.message({
                        message: '感谢你的建议',
                        type: 'info'
                    });
                    //self.location = '/';
                } else {
                    $.message({
                        message: '提交失败',
                        type: 'warning'
                    });
                }
            },
            error: function (jqXHR, textStatus, errorThrown) {
                /*错误信息处理*/
                //alert("未知错误");
                $.message({
                    message: '未知错误',
                    type: 'error'
                });
            }
        });
    }
});

$('#admin_login').on('click', function () {
    var number = $('#admin_login_number').val();
    var passwd = $('#admin_login_password').val();
    if (number == "" || passwd == "") {
        $.message({
            message: '账号或密码为空',
            type: 'warning'
        });
    } else {
        //ajax 请求
        var data = {
            "user": number,
            "passwd": passwd
        };
        $.ajax({
            url: '/admin_login/',
            type: 'POST',
            data: JSON.stringify(data),
            contentType: 'application/json; charset=UTF-8',
            dataType: 'json',
            success: function (msg) {
                //alert(msg);
                if (msg.ret == true) {
                    $.message({
                        message: '登录成功',
                        type: 'success'
                    });
                    self.location = '/admin/';
                } else {
                    $.message({
                        message: '用户名或密码错误',
                        type: 'warning'
                    });
                }
            },
            error: function (jqXHR, textStatus, errorThrown) {
                /*错误信息处理*/
                //alert("未知错误");
                $.message({
                    message: '未知错误',
                    type: 'error'
                });
            }
        });
    }
});

$('#see').on('click', function () {
    var value = $('input:radio:checked').val();
    //alert(value);
    if (value == null) {
        $.message({
            message: '没有选择座位',
            type: 'warning'
        });
    } else {
        var data = {
            "table_id": value
        };
        var span_id = "span" + value;
        var text = $('#' + span_id).text();
        //alert(span_id);
        //alert(text);
        if (text == '空闲') {
            $('#rm_info').remove();
            $('#myModal_see').modal('show');
            $('#see_info1').text('无');
            $('#see_info2').text('无');
            $('#see_info3').text('无');
            $('#see_info4').text('空闲');
        } else {
            $.ajax({
                url: '/admin/',
                type: 'POST',
                data: JSON.stringify(data),
                contentType: 'application/json; charset=UTF-8',
                dataType: 'json',
                success: function (msg) {
                    //alert(msg);
                    $('#myModal_see').modal('show');
                    if (msg.ret == "") {
                        $('#rm_info').remove();
                        $('#see_info1').text('无');
                        $('#see_info2').text('无');
                        $('#see_info3').text('无');
                        $('#see_info4').text('空闲');
                    } else {
                        //alert(msg.ret[2]);
                        var seat = msg.ret[0];
                        var num = msg.ret[1];
                        var time = msg.ret[3];
                        var leave_time = msg.ret[2];
                        //alert(seat);
                        if (seat <= 10) {
                            $('#see_info1').text('1楼' + seat + '座位');
                        } else if (seat <= 20) {
                            $('#see_info1').text('2楼' + seat + '座位');
                        } else if (seat <= 30) {
                            $('#see_info1').text('3楼' + seat + '座位');
                        } else {
                            $('#see_info1').text('4楼' + seat + '座位');
                        }

                        $('#see_info2').text(num);

                        $('#see_info3').text(time);
                        if (leave_time == 0) {
                            $('#see_info4').text('有人');
                        } else {
                            $('#see_info4').text('暂离');
                            $('#see_append_info').append("<laber id='rm_info'>暂离时间:<laber id='see_info5'></laber></laber>");
                            $('#see_info5').text(leave_time + '小时');
                        }
                    }
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    /*错误信息处理*/
                    //alert("未知错误");
                    $.message({
                        message: '未知错误',
                        type: 'error'
                    });
                }
            });
        }

    }
});

$('#clear').on('click', function () {
    //ajax 请求
    //alert("clear");
    var data = {
        "user_id": 1000
    }
    $.ajax({
        url: '/clear/',
        type: 'POST',
        data: JSON.stringify(data),
        contentType: 'application/json; charset=UTF-8',
        dataType: 'json',
        success: function (msg) {
            //alert(msg);
            if (msg.ret == true) {
                $.message({
                    message: '已清空所有',
                    type: 'info'
                });
                self.location = '/admin/';
            } else {
                $.message({
                    message: '清空失败',
                    type: 'warning'
                });
            }
        },
        error: function (jqXHR, textStatus, errorThrown) {
            /*错误信息处理*/
            //alert("未知错误");
            $.message({
                message: '未知错误',
                type: 'error'
            });
        }
    });
});

$('#close').on('click', function () {
    //ajax 请求
    $.ajax({
        url: '/close/',
        type: 'GET',
        //data: JSON.stringify(data),
        contentType: 'application/json; charset=UTF-8',
        dataType: 'json',
        success: function (msg) {
            //alert(msg);
            if (msg.ret == true) {
                $.message({
                    message: '已闭馆',
                    type: 'info'
                });
                self.location = '/admin/';
            } else {
                $.message({
                    message: '已取消闭馆',
                    type: 'warning'
                });
            }
        },
        error: function (jqXHR, textStatus, errorThrown) {
            /*错误信息处理*/
            //alert("未知错误");
            $.message({
                message: '未知错误',
                type: 'error'
            });
        }
    });
});

$('#notice').on('click', function () {
    //ajax 请求
    var title = $('#title').val();
    var context = $('#context').val();
    if (title == "" || context == "") {
        $.message({
            message: '标题或内容不能为空',
            type: 'error'
        });
    } else {
        var data = {
            "title": title,
            "context": context
        };
        $.ajax({
            url: '/notice/',
            type: 'POST',
            data: JSON.stringify(data),
            contentType: 'application/json; charset=UTF-8',
            dataType: 'json',
            success: function (msg) {
                //alert(msg);
                if (msg.ret == true) {
                    $.message({
                        message: '发布成功',
                        type: 'info'
                    });
                    //self.location = '/';
                } else {
                    $.message({
                        message: '提交失败',
                        type: 'warning'
                    });
                }
            },
            error: function (jqXHR, textStatus, errorThrown) {
                /*错误信息处理*/
                //alert("未知错误");
                $.message({
                    message: '未知错误',
                    type: 'error'
                });
            }
        });
    }
});