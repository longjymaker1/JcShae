function select_list(click_type, click_id) {
    console.log(click_type);
    console.log(click_id);
    let ids = document.getElementsByClassName('active');
    console.log('ids长度', ids.length);
    var msg_types = ids[0].name,
        provice = ids[1].name,
        city = ids[2].name;
    if (ids.length == 4){
        sort_types = ids[3].name;
    }

    if (click_type === 'msg_type'){
        msg_types = click_id;
    }else if (click_type === 'provice'){
        provice = click_id;
        city = '0';
    }else if(click_type === 'city'){
        city = click_id;
    }else{
        sort_types = click_id;
    }

    let url_arr = [sort_types, msg_types, 'provice', provice, 'city', city];
    let url_str = url_arr.join("/");
    console.log(url_str);

    $.ajax({
        // publish/t/provice/27/city/338
        url: url_str,
        type: "POST",
        data: {},
        success: function (result) {
            if (result.result == 'success'){
                console.log("发送成功!")
            }
        }
    })

}