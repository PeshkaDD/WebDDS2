// static/dds/js/main.js

$(document).ready(function() {
    // Динамическая загрузка подкатегорий при выборе категории
    $("#id_category").change(function() {
        var categoryId = $(this).val();
        if (categoryId) {
            $.ajax({
                url: "/ajax/load-subcategories/",
                data: {
                    'category': categoryId
                },
                success: function(data) {
                    $("#id_subcategory").empty();
                    $("#id_subcategory").append('<option value="">---------</option>');
                    $.each(data, function(i, item) {
                        $("#id_subcategory").append('<option value="' + item.id + '">' + item.name + '</option>');
                    });
                }
            });
        } else {
            $("#id_subcategory").empty();
            $("#id_subcategory").append('<option value="">---------</option>');
        }
    });

    // Инициализация выбора подкатегории при редактировании
    if ($("#id_subcategory").val() && $("#id_category").val()) {
        var subcategoryId = $("#id_subcategory").val();
        var categoryId = $("#id_category").val();

        $.ajax({
            url: "/ajax/load-subcategories/",
            data: {
                'category': categoryId
            },
            success: function(data) {
                $("#id_subcategory").empty();
                $("#id_subcategory").append('<option value="">---------</option>');
                $.each(data, function(i, item) {
                    var selected = (item.id == subcategoryId) ? 'selected' : '';
                    $("#id_subcategory").append('<option value="' + item.id + '" ' + selected + '>' + item.name + '</option>');
                });
            }
        });
    }
});