''' Mixins classes
'''


class MixinPageView():
    ''' Миксин вьюхи по отображению заголовка страницы
        В шаблон пенредаются следующие параметры:
        title - заголовок страницы
        table_title - заголовок таблицы
    '''
    title = ''
    head_title = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['table_title'] = self.table_title
        return context


class MixinDinamicTablesView(MixinPageView):
    ''' Микс представления страниц с динамической таблицой
        В шаблон пенредаются следующие параметры:
        data_ajax_url - url списка данных таблицы
        columns_name - список наименований колонок
        url_form_action - url action модальной формы
        fields_name - список полей формы, для передачи их в инициализацию
                      DataTable
    '''
    template_name = 'included/init_data_table.html'
    data_ajax_url = ''
    columns_name = []
    readonly = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data_ajax_url'] = self.data_ajax_url
        context['columns_name'] = self.columns_name
        context['url_form_action'] = f'/api{self.request.path}'
        context['readonly'] = self.readonly

        if not hasattr(self, 'fields_name'):
            if hasattr(self, 'form_class'):
                context['fields_name'] = self.form_class._meta.fields
        else:
            context['fields_name'] = self.fields_name
        return context
