var main = {
    init : function () {
        var _this = this;
        $('#encryptionBtn').on('click', function () {
            if($('#a').val() === ""){
                $("#errormsg").text("Key의 A 값이 비워져 있습니다!")
                $('#error').show();
                $('#success').hide();
            }
            else if($('#b').val() === ""){
                $("#errormsg").text("Key의 B 값이 비워져 있습니다!")
                $('#error').show();
                $('#success').hide();
            }
            else if($('#c').val() === ""){
                $("#errormsg").text("Key의 C 값이 비워져 있습니다!")
                $('#error').show();
                $('#success').hide();
            }
            else if($('#d').val() === ""){
                $("#errormsg").text("Key의 D 값이 비워져 있습니다!")
                $('#error').show();
                $('#success').hide();
            }
            else if($('#plainText').val() === ""){
                $("#errormsg").text("암호화 할 텍스트를 입력해주세요!")
                $('#error').show();
                $('#success').hide();
            }
            else _this.encryption();
        });
        $('#decryptionBtn').on('click', function () {
            if($('#a').val() === ""){
                $("#errormsg").text("Key의 A 값이 비워져 있습니다!")
                $('#error').show();
                $('#success').hide();
            }
            else if($('#b').val() === ""){
                $("#errormsg").text("Key의 B 값이 비워져 있습니다!")
                $('#error').show();
                $('#success').hide();
            }
            else if($('#c').val() === ""){
                $("#errormsg").text("Key의 C 값이 비워져 있습니다!")
                $('#error').show();
                $('#success').hide();
            }
            else if($('#d').val() === ""){
                $("#errormsg").text("Key의 D 값이 비워져 있습니다!")
                $('#error').show();
                $('#success').hide();
            }
            else if($('#cipherText').val() === ""){
                $("#errormsg").text("복호화 할 텍스트를 입력해주세요!")
                $('#error').show();
                $('#success').hide();
            }
            else _this.decryption();
        });
        $('#RandomkeyBtn').on('click', function () {
            _this.randomkey();
        });
        $('#pasteEnBtn').on('click', function () {
            _this.pasteEn();
        });
        $('#pasteDeBtn').on('click', function () {
            _this.pasteDe();
        });
        $('#copyEnBtn').on('click', function () {
            _this.copyEn();
        });
        $('#copyDeBtn').on('click', function () {
            _this.copyDe();
        });
    },
    encryption : function () {
        var data = {
            a: parseInt($('#a').val()),
            b: parseInt($('#b').val()),
            c: parseInt($('#c').val()),
            d: parseInt($('#d').val()),
            plain_text: $('#plainText').val()
        };
        $.ajax({
            type: 'POST',
            url: "http://127.0.0.1:18000/api/v1/hill/encryption",
            dataType: 'json',
            contentType:'application/json; charset=utf-8',
            data: JSON.stringify(data)
        }).done(function(res) {
            if (res.cipher_text) {
                $('#encryptionRes').val(res.cipher_text);
                $("#successmsg").text("성공적으로 암호화를 마쳤습니다!")
                $('#error').hide();
                $('#success').show();
            }
            else {
                $("#errormsg").text(res.message)
                $('#error').show();
                $('#success').hide();
            }
        }).fail(function (res) {
            $("#errormsg").text(res.message)
            $('#error').show();
            $('#success').hide();
        });
    },
    decryption : function () {
        var data = {
            a: parseInt($('#a').val()),
            b: parseInt($('#b').val()),
            c: parseInt($('#c').val()),
            d: parseInt($('#d').val()),
            cipher_text: $('#cipherText').val()
        };
        $.ajax({
            type: 'POST',
            url: "http://127.0.0.1:18000/api/v1/hill/decryption",
            dataType: 'json',
            contentType:'application/json; charset=utf-8',
            data: JSON.stringify(data)
        }).done(function(res) {
            if (res.plain_text) {
                $('#decryptionRes').val(res.plain_text);
                $("#successmsg").text("성공적으로 복호화를 마쳤습니다!")
                $('#error').hide();
                $('#success').show();
            }
            else {
                $("#errormsg").text(res.message)
                $('#error').show();
                $('#success').hide();
            }
        }).fail(function (res) {
            $("#errormsg").text(res.message)
            $('#error').show();
            $('#success').hide();
        });
    },
    randomkey : function () {
        $.ajax({
            type: 'GET',
            url: "http://127.0.0.1:18000/api/v1/hill/randomkey",
            dataType: 'json',
            contentType:'application/json; charset=utf-8',
        }).done(function(res) {
            $('#a').val(res.a);
            $('#b').val(res.b);
            $('#c').val(res.c);
            $('#d').val(res.d);
            $("#successmsg").text("성공적으로 키를 생성했습니다!")
            $('#error').hide();
            $('#success').show();
        }).fail(function (res) {
            $("#errormsg").text(res.message)
            $('#error').show();
            $('#success').hide();
        });
    },
    pasteEn : function () {
        navigator.clipboard.readText().then(r => { $("#plainText").val(r)});

    },
    pasteDe : function () {
        navigator.clipboard.readText().then(r => {$("#cipherText").val(r)}) ;

    },
    copyEn : function () {
        navigator.clipboard.writeText($("#encryptionRes").val()).then(r => {});

    },
    copyDe : function () {
        navigator.clipboard.writeText($("#decryptionRes").val()).then(r => {});

    },
};



main.init();