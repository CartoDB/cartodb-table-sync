from cartodb import TableSync

table_sync = TableSync('localhost', 8000)
table_sync.created('table_name_created', 'table_id_1')
table_sync.updated('table_name_updated', 'table_id_2')
table_sync.deleted('table_name_deleted', 'table_id_3')