var faqs_row = 0;
function addfaqs() {
html = '<tr id="faqs-row' + faqs_row + '">';
    html += '<td><select name="propertytype" class="form-control"><option selected="true" disabled="disabled">Product</option>{% for value in product %}<option value="{{ value }}">{{ value }}</option>{% endfor %}</select></td>';
    html += '<td><input type="text" placeholder="Quantity" class="form-control"></td>';
    html += '<td><input type="text" placeholder="Price" class="form-control"></td>';
    html += '<td class="mt-10"><button class="badge badge-danger" onclick="$(\'#faqs-row' + faqs_row + '\').remove();"><i class="fa fa-trash"></i> Remove </button></td>';

    html += '</tr>';

$('#faqs tbody').append(html);

faqs_row++;}