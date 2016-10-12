/*
Utilities for converting KBaseAssembly types to KBaseFile types
*/

module kb_ea_utils {

/*

		This module has methods to  get fastq statistics
		workspace_name    - the name of the workspace for input/output
		read_library_name - the name of  KBaseFile.SingleEndLibrary or
                        KBaseFile.PairedEndLibrary

*/


typedef structure {
		string workspace_name;
		string read_library_name;
} get_fastq_ea_utils_stats_params;


/*
 This function should be used for getting statistics on read library object types 
 The results are returned as a string.
*/

funcdef get_fastq_ea_utils_stats (get_fastq_ea_utils_stats_params input_params)
        returns (string ea_utils_stats)
authentication required; 


typedef structure {
		string report_name;
		string report_ref;
} Report;


typedef structure {
		string workspace_name;
		string read_library_name;
} run_app_fastq_ea_utils_stats_params;

/*
 This function should be used for getting statistics on read library object type.
 The results are returned as a report type object.
*/


funcdef run_app_fastq_ea_utils_stats (run_app_fastq_ea_utils_stats_params input_params)
        returns (Report report)
authentication required; 


/*
    read_library_path : absolute path of fastq files
*/

typedef structure {
		string read_library_path;
} ea_utils_params;

/*
 This function should be used for getting statistics on fastq files. Input is string of file path
*/

funcdef get_ea_utils_stats (ea_utils_params input_params)
        returns (string report)
authentication required; 





};
