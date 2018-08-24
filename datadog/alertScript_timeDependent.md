{{#is_alert}} 

ALERT: my_metric has averaged more than 800 for the last 5 minutes! 

Host IP {{host.ip}} has reported an average value of 

{{"q": "my_metric{host:ubuntu-xenial}.rollup(avg,300)"}} 
{{my_metric{host:ubuntu-xenial}.rollup(avg,300)}} 
during that time.

{{/is_alert}}



{{#is_warning}} Warning: Host IP {{host.ip}} reports that my_metric has averaged more than 500 for the last 5 minutes! {{/is_warning}}



{{#is_no_data}} 
Warning! No data has been reported by my_metric on Host IP {{host.ip}} in the last 10 minutes!
{{/is_no_data}}

{{#ifdayisSATorSUN}}
{{#somethingsomethingDateTime_9am_to_7pm_M-F}}

Notify: @BradleyShields (probably)

{{/somethingsomethingDateTime_9am_to_7pm_M-F}}
{{/ifdayisSATorSUN}}

Before submitting this one, on section 5 (take screen shot of 5 with this setting) set DO NOTIFY reipients when alert modified. Then, screen shot of email hitting your email.
