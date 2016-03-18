char *strReplace(const char *src, const char *from, const char *to)
{
char *value;
char *dst;
char *match;
int size;
int fromlen;
int tolen;
// Find out the lengths of the source string, text to replace, and
// the replacement text.
size = strlen(src) + 1;
fromlen = strlen(from);
tolen = strlen(to);
// Allocate the first chunk with enough for the original string.
value = (char *)malloc(size);
// We need to return 'value', so let's make a copy to mess around with.
dst = value;
// Before we begin, let's see if malloc was successful.
if ( value != NULL )
{
// Loop until no matches are found.
for ( ;; )
{
// Try to find the search text.
match = (char *) strstr(src, from);
if ( match != NULL )
{
// Found search text at location 'match'.
// Find out how many characters to copy up to the 'match'.
size_t count = match - src;
// We are going to realloc, and for that we will need a
// temporary pointer for safe usage.
char *temp;
// Calculate the total size the string will be after the
// replacement is performed.
size += tolen - fromlen;
// Attempt to realloc memory for the new size.
//
// temp = realloc(value, size);
temp = (char *)realloc(value, size);
if ( temp == NULL )
{
// Attempt to realloc failed. Free the previously malloc'd
// memory and return with our tail between our legs.
free(value);
return NULL;
}
// The call to realloc was successful. But we'll want to
// return 'value' eventually, so let's point it to the memory
// that we are now working with. And let's not forget to point
// to the right location in the destination as well.
dst = temp + (dst - value);
value = temp;
// Copy from the source to the point where we matched. Then
// move the source pointer ahead by the amount we copied. And
// move the destination pointer ahead by the same amount.
memmove(dst, src, count);
src += count;
dst += count;
// Now copy in the replacement text 'to' at the position of
// the match. Adjust the source pointer by the text we replaced.
// Adjust the destination pointer by the amount of replacement
// text.
memmove(dst, to, tolen);
src += fromlen;
dst += tolen;
}
else // No match found.
{
// Copy any remaining part of the string. This includes the null
// termination character.
strcpy(dst, src);
break;
}
} // For Loop()
}
return value;
}
// ----------------------------------------------------------------------------
//
// Description:
// Find and replace text within a LoadRunner string.
//
// Parameters:
// lrparam (in) - pointer to LoadRunner Parameter Name
// findstr (in) - pointer to text top search for
// replacestr (in) - pointer to text to use as replacement
//
// Returns:
// Returns an integer. 0=Error, 1=Success.
//
// Example:
// lr_save_string( "This is a small test of the search and replace function", "LRParam");
// lr_replace( "LRParam", "a", "-x-" );
// lr_output_message( "%s", lr_eval_string("{LRParam}") );
//
// ----------------------------------------------------------------------------
int lr_replace( const char *lrparam, char *findstr, char *replacestr )
{
int res = 0;
char *result_str;
char lrp[1024];
// Finalize the LR Param Name
sprintf( lrp, "{%s}", lrparam);
// Do the Search and Replace
result_str = strReplace( lr_eval_string(lrp), findstr, replacestr );
// Process results
if (result_str != NULL )
{
lr_save_string( result_str, lrparam );
free( result_str );
res = 1;
}
return res;
} // EOF