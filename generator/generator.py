
import os
from conf.conf_files import conf
from conf.filter_structure import filter_structure
# import blocks_header_constructor as header_const
from blocks_header_constructor import filter_header, header_block

dirname = os.path.dirname(__file__)
export_folder = os.path.join(dirname, 'output')
blocks_folder = os.path.join(dirname, 'filter-blocks')
blocks_extension = '.filter'

def fwrite_lines(wf, rf) :
  with open(rf, "r") as rfile:
      for line in rfile:
          wf.write(line)

# --- Function Construct (...)
def construct(filt_structure, conf_list):

  for conf_obj in conf_list :

    export_file = os.path.join(export_folder, conf_obj.get('name') + '.filter')
    
    with open(export_file, "w") as file :

      for obj in filt_structure :  

        match obj.get('type'):
          
          case 'filter-header': 
            
            fheader_title = 'My Poe2 filter | ' + conf_obj.get('name') + ' | ' + conf_obj.get('strictness')
            fheader_version = conf_obj.get('version')
            fheader_author = conf_obj.get('author')
            fheader_desc = conf_obj.get('description')
            
            file.write ( filter_header ( fheader_title , fheader_version, fheader_author, fheader_desc ) )

          case 'filter-index': 
            
            rfile = os.path.join(blocks_folder, 'index.filter')

            with open(rfile, "r") as rf :
              for line in rf :
                file.write(line)

          case 'header': 

            h_data = obj.get('header-data')

            file.write ( header_block ( h_data.get('type'), h_data.get('index'), h_data.get('text'), h_data.get('tags') ) )

          case 'block': 

            files = obj.get('files')

            for row in files :

              if row.get('strictness') == conf_obj.get('strictness') :

                rfile = os.path.join(blocks_folder, row.get('file') + '.filter')

                with open(rfile, "r") as rf :
                  for line in rf :
                    file.write(line)

              else :
                pass

          case 'class-block' :
            
            subtype = obj.get('subtype')

            # print( conf.get ( obj.get('subtype' ) ) )
            for class_obj in obj.get('classes'):
              
              for item_class in conf_obj.get(subtype) :

                if class_obj.get('condition') == item_class:
                
                  for row in class_obj.get('files') :

                    if row.get('strictness') == conf_obj.get('strictness') :

                      rfile = os.path.join(blocks_folder, row.get('file') + '.filter')

                      with open(rfile, "r") as rf :
                        for line in rf :
                          file.write(line)

          case _: print('---------- NO CASE')

construct(filter_structure, conf)

# for config in conf:
#   print(filter_header(config.get('name'), config.get('version'), config.get('author'), config.get('description')))
#   print(header_block('3', '0005', 'test', '#test-tags'))


# init

# construct(file_structure, '')