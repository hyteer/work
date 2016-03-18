# 1 "e:\\test\\temp\\einvoice0318\\\\combined_eInvoice0318.c"
# 1 "globals.h" 1
 
 
# 1 "C:\\Program Files\\HP\\LoadRunner\\include/lrun.h" 1
 
 












 











# 103 "C:\\Program Files\\HP\\LoadRunner\\include/lrun.h"








































































	

 


















 
 
 
 
 


 
 
 
 
 
 














int     lr_start_transaction   (char * transaction_name);
int lr_start_sub_transaction          (char * transaction_name, char * trans_parent);
long lr_start_transaction_instance    (char * transaction_name, long parent_handle);



int     lr_end_transaction     (char * transaction_name, int status);
int lr_end_sub_transaction            (char * transaction_name, int status);
int lr_end_transaction_instance       (long transaction, int status);


 
typedef char* lr_uuid_t;
 



lr_uuid_t lr_generate_uuid();

 


int lr_generate_uuid_free(lr_uuid_t uuid);

 



int lr_generate_uuid_on_buf(lr_uuid_t buf);

   
# 263 "C:\\Program Files\\HP\\LoadRunner\\include/lrun.h"
int lr_start_distributed_transaction  (char * transaction_name, lr_uuid_t correlator, long timeout  );

   







int lr_end_distributed_transaction  (lr_uuid_t correlator, int status);


double lr_stop_transaction            (char * transaction_name);
double lr_stop_transaction_instance   (long parent_handle);


void lr_resume_transaction           (char * trans_name);
void lr_resume_transaction_instance  (long trans_handle);


int lr_update_transaction            (const char *trans_name);


 
void lr_wasted_time(long time);


 
int lr_set_transaction(const char *name, double duration, int status);
 
long lr_set_transaction_instance(const char *name, double duration, int status, long parent_handle);


int   lr_user_data_point                      (char *, double);
long lr_user_data_point_instance                   (char *, double, long);
 



int lr_user_data_point_ex(const char *dp_name, double value, int log_flag);
long lr_user_data_point_instance_ex(const char *dp_name, double value, long parent_handle, int log_flag);


int lr_transaction_add_info      (const char *trans_name, char *info);
int lr_transaction_instance_add_info   (long trans_handle, char *info);
int lr_dpoint_add_info           (const char *dpoint_name, char *info);
int lr_dpoint_instance_add_info        (long dpoint_handle, char *info);


double lr_get_transaction_duration       (char * trans_name);
double lr_get_trans_instance_duration    (long trans_handle);
double lr_get_transaction_think_time     (char * trans_name);
double lr_get_trans_instance_think_time  (long trans_handle);
double lr_get_transaction_wasted_time    (char * trans_name);
double lr_get_trans_instance_wasted_time (long trans_handle);
int    lr_get_transaction_status		 (char * trans_name);
int	   lr_get_trans_instance_status		 (long trans_handle);

 



int lr_set_transaction_status(int status);

 



int lr_set_transaction_status_by_name(int status, const char *trans_name);
int lr_set_transaction_instance_status(int status, long trans_handle);


typedef void* merc_timer_handle_t;
 

merc_timer_handle_t lr_start_timer();
double lr_end_timer(merc_timer_handle_t timer_handle);


 
 
 
 
 
 











 



int   lr_rendezvous  (char * rendezvous_name);
 




int   lr_rendezvous_ex (char * rendezvous_name);



 
 
 
 
 
char *lr_get_vuser_ip (void);
void   lr_whoami (int *vuser_id, char ** sgroup, int *scid);
char *	  lr_get_host_name (void);
char *	  lr_get_master_host_name (void);

 
long     lr_get_attrib_long	(char * attr_name);
char *   lr_get_attrib_string	(char * attr_name);
double   lr_get_attrib_double      (char * attr_name);

char * lr_paramarr_idx(const char * paramArrayName, unsigned int index);
char * lr_paramarr_random(const char * paramArrayName);
int    lr_paramarr_len(const char * paramArrayName);

int	lr_param_unique(const char * paramName);
int lr_param_sprintf(const char * paramName, const char * format, ...);


 
 
static void *ci_this_context = 0;






 








void lr_continue_on_error (int lr_continue);
char *   lr_decrypt (const char *EncodedString);


 
 
 
 
 
 



 







 















void   lr_abort (void);
void lr_exit(int exit_option, int exit_status);
void lr_abort_ex (unsigned long flags);

void   lr_peek_events (void);


 
 
 
 
 


void   lr_think_time (double secs);

 


void lr_force_think_time (double secs);


 
 
 
 
 



















int   lr_msg (char * fmt, ...);
int   lr_debug_message (unsigned int msg_class,
									    char * format,
										...);
# 502 "C:\\Program Files\\HP\\LoadRunner\\include/lrun.h"
void   lr_new_prefix (int type,
                                 char * filename,
                                 int line);
# 505 "C:\\Program Files\\HP\\LoadRunner\\include/lrun.h"
int   lr_log_message (char * fmt, ...);
int   lr_message (char * fmt, ...);
int   lr_error_message (char * fmt, ...);
int   lr_output_message (char * fmt, ...);
int   lr_vuser_status_message (char * fmt, ...);
int   lr_error_message_without_fileline (char * fmt, ...);
int   lr_fail_trans_with_error (char * fmt, ...);

 
 
 
 
 
# 528 "C:\\Program Files\\HP\\LoadRunner\\include/lrun.h"

 
 
 
 
 





int   lr_next_row ( char * table);
int lr_advance_param ( char * param);



														  
														  

														  
														  

													      
 


char *   lr_eval_string (char * str);
int   lr_eval_string_ext (const char *in_str,
                                     unsigned long const in_len,
                                     char ** const out_str,
                                     unsigned long * const out_len,
                                     unsigned long const options,
                                     const char *file,
								     long const line);
# 562 "C:\\Program Files\\HP\\LoadRunner\\include/lrun.h"
void   lr_eval_string_ext_free (char * * pstr);

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
int lr_param_increment (char * dst_name,
                              char * src_name);
# 585 "C:\\Program Files\\HP\\LoadRunner\\include/lrun.h"













											  
											  

											  
											  
											  

int	  lr_save_var (char *              param_val,
							  unsigned long const param_val_len,
							  unsigned long const options,
							  char *			  param_name);
# 609 "C:\\Program Files\\HP\\LoadRunner\\include/lrun.h"
int   lr_save_string (const char * param_val, const char * param_name);
int   lr_free_parameter (const char * param_name);
int   lr_save_int (const int param_val, const char * param_name);


 
 
 
 
 
 
# 676 "C:\\Program Files\\HP\\LoadRunner\\include/lrun.h"
void   lr_save_datetime (const char *format, int offset, const char *name);









 











 
 
 
 
 






 



char * lr_error_context_get_entry (char * key);

 



long   lr_error_context_get_error_id (void);


 
 
 

int lr_table_get_rows_num (char * param_name);

int lr_table_get_cols_num (char * param_name);

char * lr_table_get_cell_by_col_index (char * param_name, int row, int col);

char * lr_table_get_cell_by_col_name (char * param_name, int row, const char* col_name);

int lr_table_get_column_name_by_index (char * param_name, int col, 
											char * * const col_name,
											int * col_name_len);
# 737 "C:\\Program Files\\HP\\LoadRunner\\include/lrun.h"

int lr_table_get_column_name_by_index_free (char * col_name);


 
 
 
 
 
 
 
 

 
 
 
 
 
 
int   lr_param_substit (char * file,
                                   int const line,
                                   char * in_str,
                                   int const in_len,
                                   char * * const out_str,
                                   int * const out_len);
# 762 "C:\\Program Files\\HP\\LoadRunner\\include/lrun.h"
void   lr_param_substit_free (char * * pstr);


 
# 774 "C:\\Program Files\\HP\\LoadRunner\\include/lrun.h"





char *   lrfnc_eval_string (char * str,
                                      char * file_name,
                                      long const line_num);
# 782 "C:\\Program Files\\HP\\LoadRunner\\include/lrun.h"


int   lrfnc_save_string ( const char * param_val,
                                     const char * param_name,
                                     const char * file_name,
                                     long const line_num);
# 788 "C:\\Program Files\\HP\\LoadRunner\\include/lrun.h"

int   lrfnc_free_parameter (const char * param_name );

int lr_save_searched_string(char *buffer, long buf_size, unsigned int occurrence,
			    char *search_string, int offset, unsigned int param_val_len, 
			    char *param_name);

 
char *   lr_string (char * str);

 
# 859 "C:\\Program Files\\HP\\LoadRunner\\include/lrun.h"

int   lr_save_value (char * param_val,
                                unsigned long const param_val_len,
                                unsigned long const options,
                                char * param_name,
                                char * file_name,
                                long const line_num);
# 866 "C:\\Program Files\\HP\\LoadRunner\\include/lrun.h"


 
 
 
 
 











int   lr_printf (char * fmt, ...);
 
int   lr_set_debug_message (unsigned int msg_class,
                                       unsigned int swtch);
# 888 "C:\\Program Files\\HP\\LoadRunner\\include/lrun.h"
unsigned int   lr_get_debug_message (void);


 
 
 
 
 

void   lr_double_think_time ( double secs);
void   lr_usleep (long);


 
 
 
 
 
 




int *   lr_localtime (long offset);


int   lr_send_port (long port);


# 964 "C:\\Program Files\\HP\\LoadRunner\\include/lrun.h"



struct _lr_declare_identifier{
	char signature[24];
	char value[128];
};

int   lr_pt_abort (void);

void vuser_declaration (void);






# 993 "C:\\Program Files\\HP\\LoadRunner\\include/lrun.h"


# 1005 "C:\\Program Files\\HP\\LoadRunner\\include/lrun.h"
















 
 
 
 
 







int    _lr_declare_transaction   (char * transaction_name);


 
 
 
 
 







int   _lr_declare_rendezvous  (char * rendezvous_name);

 
 
 
 
 

 
int lr_enable_ip_spoofing();
int lr_disable_ip_spoofing();


 




int lr_convert_string_encoding(char *sourceString, char *fromEncoding, char *toEncoding, char *paramName);





 
 

















# 3 "globals.h" 2

# 1 "C:\\Program Files\\HP\\LoadRunner\\include/as_web.h" 1
 






















































 




 








 
 
 

  int
	web_add_filter(
		const char *		mpszArg,
		...
	);									 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 

  int
	web_add_auto_filter(
		const char *		mpszArg,
		...
	);									 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
	
  int
	web_add_auto_header(
		const char *		mpszHeader,
		const char *		mpszValue);

  int
	web_add_header(
		const char *		mpszHeader,
		const char *		mpszValue);
  int
	web_add_cookie(
		const char *		mpszCookie);
  int
	web_cleanup_auto_headers(void);
  int
	web_cleanup_cookies(void);
  int
	web_concurrent_end(
		const char * const	mpszReserved,
										 
		...								 
	);
  int
	web_concurrent_start(
		const char * const	mpszConcurrentGroupName,
										 
										 
		...								 
										 
	);
  int
	web_create_html_param(
		const char *		mpszParamName,
		const char *		mpszLeftDelim,
		const char *		mpszRightDelim);
  int
	web_create_html_param_ex(
		const char *		mpszParamName,
		const char *		mpszLeftDelim,
		const char *		mpszRightDelim,
		const char *		mpszNum);
  int
	web_custom_request(
		const char *		mpszReqestName,
		...);							 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
  int
	web_disable_keep_alive(void);
  int
	web_enable_keep_alive(void);
  int
	web_find(
		const char *		mpszStepName,
		...);							 
										 
										 
										 
										 
										 
										 
										 
										 
										 
  int
	web_get_int_property(
		const int			miHttpInfoType);
  int
	web_image(
		const char *		mpszStepName,
		...);							 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
  int
	web_image_check(
		const char *		mpszName,
		...);
  int
	web_java_check(
		const char *		mpszName,
		...);
  int
	web_link(
		const char *		mpszStepName,
		...);							 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 

	
  int
	web_global_verification(
		const char *		mpszArg1,
		...);							 
										 
										 
										 
										 
										 

  int
	web_reg_find(
		const char *		mpszArg1,
		...);							 
										 
										 
										 
										 
										 
										 
										 
				
  int
	web_reg_save_param(
		const char *		mpszParamName,
		...);							 
										 
										 
										 
										 
										 
										 

  int
	web_convert_param(
		const char * 		mpszParamName, 
										 
		...);							 
										 
										 


										 

										 
  int
	web_remove_auto_filter(
		const char *		mpszArg,
		...
	);									 
										 
				
  int
	web_remove_auto_header(
		const char *		mpszHeaderName,
		...);							 
										 



  int
	web_remove_cookie(
		const char *		mpszCookie);

  int
	web_save_header(
		const char *		mpszType,	 
		const char *		mpszName);	 
  int
	web_set_certificate(
		const char *		mpszIndex);
  int
	web_set_certificate_ex(
		const char *		mpszArg1,
		...);							 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
  int
	web_set_connections_limit(
		const char *		mpszLimit);
  int
	web_set_max_html_param_len(
		const char *		mpszLen);
  int
	web_set_max_retries(
		const char *		mpszMaxRetries);
  int
	web_set_proxy(
		const char *		mpszProxyHost);
  int
	web_set_proxy_bypass(
		const char *		mpszBypass);
  int
	web_set_secure_proxy(
		const char *		mpszProxyHost);
  int
	web_set_sockets_option(
		const char *		mpszOptionID,
		const char *		mpszOptionValue
	);
  int
	web_set_option(
		const char *		mpszOptionID,
		const char *		mpszOptionValue,
		...								 
	);
  int
	web_set_timeout(
		const char *		mpszWhat,
		const char *		mpszTimeout);
  int
	web_set_user(
		const char *		mpszUserName,
		const char *		mpszPwd,
		const char *		mpszHost);

  int
	web_sjis_to_euc_param(
		const char *		mpszParamName,
										 
		const char *		mpszParamValSjis);
										 

  int
	web_submit_data(
		const char *		mpszStepName,
		...);							 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
  int
	web_submit_form(
		const char *		mpszStepName,
		...);							 
										 
										 
										 
										 
										 
										 
										 
										 
										  
										 
										 
										 
										 
										 
										  
										 
										 
										 
										 
										 
										 
										 
										  
										 
										 
										 
										 
										 
										  
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
  int
	web_url(
		const char *		mpszUrlName,
		...);							 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 

  int 
	web_set_proxy_bypass_local(
		const char * mpszNoLocal
		);

  int 
	web_cache_cleanup(void);

  int
	web_create_html_query(
		const char* mpszStartQuery,
		...);							 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 

  int 
	web_create_radio_button_param(
		const char *NameFiled,
		const char *NameAndVal,
		const char *ParamName
		);

  int
	web_convert_from_formatted(
		const char * mpszArg1,
		...);							 
										 
										 
										 
										 
										 
										
  int
	web_convert_to_formatted(
		const char * mpszArg1,
		...);							 
										 
										 
										 
										 
										 

  int
	web_reg_save_param_ex(
		const char * mpszParamName,
		...);							 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 

  int
	web_reg_save_param_xpath(
		const char * mpszParamName,
		...);							
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 
										 










# 596 "C:\\Program Files\\HP\\LoadRunner\\include/as_web.h"


# 609 "C:\\Program Files\\HP\\LoadRunner\\include/as_web.h"



























# 647 "C:\\Program Files\\HP\\LoadRunner\\include/as_web.h"

 
 
 


  int
	FormSubmit(
		const char *		mpszFormName,
		...);
  int
	InitWebVuser(void);
  int
	SetUser(
		const char *		mpszUserName,
		const char *		mpszPwd,
		const char *		mpszHost);
  int
	TerminateWebVuser(void);
  int
	URL(
		const char *		mpszUrlName);
























# 715 "C:\\Program Files\\HP\\LoadRunner\\include/as_web.h"



 
 
 






# 4 "globals.h" 2

# 1 "C:\\Program Files\\HP\\LoadRunner\\include/lrw_custom_body.h" 1
 





# 5 "globals.h" 2

# 1 "C:\\Program Files\\HP\\LoadRunner\\include/wssoap.h" 1
 










 
# 77 "C:\\Program Files\\HP\\LoadRunner\\include/wssoap.h"


  int
soap_request(
				char * pFirstArg,
				...
			);


 




























 






 
# 238 "C:\\Program Files\\HP\\LoadRunner\\include/wssoap.h"


  int
web_service_call(
					char * pFirstArg,	
					...
				);



 
# 272 "C:\\Program Files\\HP\\LoadRunner\\include/wssoap.h"


  int
web_service_set_security(
					char * pFirstArg,	
					...
				);

 
# 305 "C:\\Program Files\\HP\\LoadRunner\\include/wssoap.h"


  char*
web_service_wait_for_event(
					char * pFirstArg,	
					...
 
				);

 






  int
web_service_cancel_security();

 
# 334 "C:\\Program Files\\HP\\LoadRunner\\include/wssoap.h"


  int
wsdl_wsi_validation (
					 char * pFirstArg,	
					...
				);

 
# 380 "C:\\Program Files\\HP\\LoadRunner\\include/wssoap.h"


  int
web_service_set_security_saml(
					char * pFirstArg,	
					...
				);


 






  int
web_service_cancel_security_saml();

 
# 412 "C:\\Program Files\\HP\\LoadRunner\\include/wssoap.h"

  int
jms_send_message_queue(
					    const char * StepName,
						const char * SentMessage,
						const char * SendQueueName);



  int
jms_receive_message_queue(
						  const char * StepName,
						  const char * ReceiveQueueName);


  int
jms_send_receive_message_queue(
					const char * StepName,
					const char * SentMessage,
					const char * SendQueueName,
					const char * ReceiveQueueName);


  int
jms_publish_message_topic(
					   const char * StepName,
					   const char * SentMessage,
					   const char * SendTopicName);


  int
jms_receive_message_topic(
						  const char * StepName,
						  const char * SubscriptionName,
						  const char * ReceiveTopicName);

  int
jms_subscribe_topic(
					const char * StepName,
					const char * SubscriptionName,
					const char * SendTopicName);

  int
jms_set_general_property(
						 const char * StepName,
					const char * Name,
					const char * Value);

  int
jms_set_message_property(
						 const char * StepName,
						const char * name,
						const char * value);

						
 











  int
soa_xml_validate (
					char * pFirstArg,	
					...
				  );

  int
lr_db_connect (
					char * pFirstArg,	
					...
				  );
  int
lr_db_disconnect (
					char * pFirstArg,	
					...
				  );
  int
lr_db_executeSQLStatement (
					char * pFirstArg,	
					...
				  );


  int
lr_db_dataset_action (
					char * pFirstArg,	
					...
				  );

  int
lr_checkpoint (
					char * pFirstArg,	
					...
				  );

  int
lr_db_getvalue (
					char * pFirstArg,	
					...
				  );


# 6 "globals.h" 2


 
 
# 1 "e:\\test\\temp\\einvoice0318\\\\combined_eInvoice0318.c" 2


# 1 "globals.h" 1
 
 


# 1 "C:\\Program Files\\HP\\LoadRunner\\include/lrw_custom_body.h" 1
 





# 5 "globals.h" 2



 
 
# 3 "e:\\test\\temp\\einvoice0318\\\\combined_eInvoice0318.c" 2

# 1 "vuser_init.c" 1
vuser_init()
{
	return 0;
}
# 4 "e:\\test\\temp\\einvoice0318\\\\combined_eInvoice0318.c" 2

# 1 "Action.c" 1
# 1 "replace.h" 1
char *strReplace(const char *src, const char *from, const char *to)
{
char *value;
char *dst;
char *match;
int size;
int fromlen;
int tolen;
 
 
size = strlen(src) + 1;
fromlen = strlen(from);
tolen = strlen(to);
 
value = (char *)malloc(size);
 
dst = value;
 
if ( value != 0 )
{
 
for ( ;; )
{
 
match = (char *) strstr(src, from);
if ( match != 0 )
{
 
 
int count = match - src;
 
 
char *temp;
 
 
size += tolen - fromlen;
 
 
 
temp = (char *)realloc(value, size);
if ( temp == 0 )
{
 
 
free(value);
return 0;
}
 
 
 
 
dst = temp + (dst - value);
value = temp;
 
 
 
memmove(dst, src, count);
src += count;
dst += count;
 
 
 
 
memmove(dst, to, tolen);
src += fromlen;
dst += tolen;
}
else  
{
 
 
strcpy(dst, src);
break;
}
}  
}
return value;
}
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
int lr_replace( const char *lrparam, char *findstr, char *replacestr )
{
int res = 0;
char *result_str;
char lrp[1024];
 
sprintf( lrp, "{%s}", lrparam);
 
result_str = strReplace( lr_eval_string(lrp), findstr, replacestr );
 
if (result_str != 0 )
{
lr_save_string( result_str, lrparam );
free( result_str );
res = 1;
}
return res;
}  
# 1 "Action.c" 2

# 1 "yt.h" 1

char *yt="YT test";
char *xml_res;
char *xml_test_res;
int xml_test;
char *xml_test2;
char *xml_input;



 

# 2 "Action.c" 2

Action()
{
	web_set_proxy("127.0.0.1:8888");

	lr_start_transaction("kp"); 




	web_service_call( "StepName=electronInvoice_102",
		"SOAPMethod=ElectronInvoiceSer|ElectronInvoiceSerHttpPort|electronInvoice",
		"ResponseParam=response",
		"Service=ElectronInvoiceSer",
		"ExpectedResponse=SoapResult",
		"Snapshot=t1457769024.inf",
		"BEGIN_ARGUMENTS",
		"xml=<ElectronInvoiceInput><UNI_BSS_HEAD><ORIG_DOMAIN>PTIS</ORIG_DOMAIN><SERVICE_NAME>ElectronInvoiceSer</SERVICE_NAME><OPERATE_NAME>electronInvoice</OPERATE_NAME><ACTION_CODE>0</ACTION_CODE><ACTION_RELATION>0</ACTION_RELATION><ROUTING><ROUTE_TYPE>36</ROUTE_TYPE><ROUTE_VALUE>18674453342</ROUTE_VALUE></ROUTING><PROC_ID>seq00001</PROC_ID><TRANS_IDO>seq00001</TRANS_IDO><TRANS_IDH></TRANS_IDH><PROCESS_TIME>201603111704001</PROCESS_TIME><RESPONSE><RSP_TYPE></RSP_TYPE><RSP_CODE></RSP_CODE><RSP_DESC></RSP_DESC></RESPONSE><COM_BUS_INFO><OPER_ID>yanff</OPER_ID><PROVINCE_CODE>0002</PROVINCE_CODE><EPARCHY_CODE>地市代码表</EPARCHY_CODE><CITY_CODE>区县编码</CITY_CODE><CHANNEL_ID>渠道编码</CHANNEL_ID><ACCESS_TYPE>1</ACCESS_TYPE><ORDER_TYPE>1</ORDER_TYPE></COM_BUS_INFO><SP_RESERVE><TRANS_IDC>ECIP0002seq00001</TRANS_IDC><CUTOFFDAY>20080608</CUTOFFDAY><OSNDUNS>0002</OSNDUNS><HSNDUNS>1100</HSNDUNS><CONV_ID>ECIP0002seq00001200806081200111</CONV_ID></SP_RESERVE><TEST_FLAG>0</TEST_FLAG><MSG_SENDER>1100</MSG_SENDER><MSG_RECEIVER>1101</MSG_RECEIVER></UNI_BSS_HEAD><UNI_BSS_BODY><ELECTRON_INVOICE_REQ><INVOICE_REQ_ID>lyl{lsh}</INVOICE_REQ_ID><MAKE_INVOICE_TYPE>0</MAKE_INVOICE_TYPE><SELLER_TAXPAYER_ID>440300568519737</SELLER_TAXPAYER_ID><SELLER_NAME>电子发票测试-LR</SELLER_NAME><SELLER_ADD>深圳市南山区南海大道1057号科技大厦二期A栋601房</SELLER_ADD><SELLER_PHONE>0755-26027907</SELLER_PHONE><SELLER_BANK_ACCOUNT>31001669701052502638</SELLER_BANK_ACCOUNT><BUYER_TAXPAYER_ID></BUYER_TAXPAYER_ID><BUYER_NAME>张三</BUYER_NAME><BUYER_ADD>深圳市南山区深南大道1057号科技大厦二期A栋6888房</BUYER_ADD><BUYER_BANK_ACCOUNT>98888888701052502638</BUYER_BANK_ACCOUNT><BUYER_PHONE>18888888888</BUYER_PHONE><BUYER_EMAIL>test@fapiao.com</BUYER_EMAIL><WRITE_MANAGER>admin</WRITE_MANAGER><RECE_FEE_MANAGER>admin</RECE_FEE_MANAGER><CHECK_MANAGER>admin</CHECK_MANAGER><ORG_INVOICE_CODE></ORG_INVOICE_CODE><ORG_INVOICE_NUM></ORG_INVOICE_NUM><TOTAL_PRICE_TAX>117</TOTAL_PRICE_TAX><TOTAL_FEE>100</TOTAL_FEE><TOTAL_TAX_PAY>17</TOTAL_TAX_PAY><PROJECT_INFO><INVOICE_COMPANY_NATURE>0</INVOICE_COMPANY_NATURE><PROJECT_NAME>洗衣粉</PROJECT_NAME><UNIT>袋</UNIT><MODEL>500克</MODEL><PROJECT_COUNT>1</PROJECT_COUNT><PROJECT_UNIT_PRICE>100</PROJECT_UNIT_PRICE><PROJECT_FEE>100</PROJECT_FEE><TAX_RATE>0.17</TAX_RATE><TAX_PAY>17</TAX_PAY></PROJECT_INFO><PARA><PARA_ID>保留字段ID</PARA_ID><PARA_VALUE>保留字段值</PARA_VALUE></PARA></ELECTRON_INVOICE_REQ></UNI_BSS_BODY><UNI_BSS_ATTACHED><MEDIA_INFO></MEDIA_INFO></UNI_BSS_ATTACHED></ElectronInvoiceInput>",
		"END_ARGUMENTS",
		"BEGIN_RESULT",
		"out=Param_out",
		"END_RESULT",
		"LAST");


	lr_output_message("【ResponseValue】:%s", lr_eval_string("{Param_out}"));

	lr_save_string( lr_eval_string("{Param_out}"),"res" );
    
	

	 
	
 

	lr_replace("res","&lt;","<" );
	lr_replace( "res","&gt;",">" );
	xml_res=lr_eval_string("{res}");
	lr_output_message("【Converted Value】:%s", xml_res);


 

 
 
	
	lr_convert_string_encoding(xml_res,0,"utf-8","xml_res_utf8"); 

	lr_output_message("【Test-ElectronInoice-UTF8】:%s",lr_eval_string("{xml_res_utf8}"));

    lr_xml_get_values("XML={xml_res_utf8}",
          "ValueParam=XML_Result",
          "Query=/ElectronInvoiceOutput/UNI_BSS_BODY/ELECTRON_INVOICE_RSP/RESP_CODE",
          "LAST" );

	lr_xml_get_values("XML={xml_res_utf8}",
          "ValueParam=XML_InvoiceAddr",
          "Query=//INVOICE_URL",
          "LAST" );


     lr_output_message(lr_eval_string("【Result】: Success! <RESP_CODE> is= {XML_Result}"));
	 lr_output_message(lr_eval_string("【Invoice Address】: = {XML_InvoiceAddr}"));


	  


   
   
	
	if(atoi(lr_eval_string("{XML_Result}"))==0){
      lr_output_message("WebService调用成功！");
      
	  lr_end_transaction("kp", 2);

	}
	else{
      lr_error_message("WebService调用失败！");
     
	  lr_end_transaction("kp", 2);

	}


return 0;
}
# 5 "e:\\test\\temp\\einvoice0318\\\\combined_eInvoice0318.c" 2

# 1 "vuser_end.c" 1
vuser_end()
{
	return 0;
}
# 6 "e:\\test\\temp\\einvoice0318\\\\combined_eInvoice0318.c" 2

