import pandas as pd
class Annotations_parser:
    def __init__(self, annotation_html: dict) -> None:
        self.annotations_html = annotation_html
        self.annotations_list = []    
    def get_annotations(self):
        
        for annotation_software, html in self.annotations_html.items():
            annotations_dataframes = pd.read_html(html)
            all_annotations_df = annotations_dataframes[0]
            #noncanoncial_interactions = annotations_dataframes[1]
            #stacking_interactions = annotations_dataframes[2]

            all_annotations_df.set_index("Base pair", inplace=True)
            all_annotations_df.drop("Represented in dot-bracket?", axis=1, inplace=True)
            all_annotations_df = all_annotations_df.add_prefix(f"{annotation_software}-")

            self.annotations_list.append(all_annotations_df)
    
        self.annotations_dataframe = self.annotations_list[0]
        for d in self.annotations_list[1:]:
            self.annotations_dataframe = self.annotations_dataframe.merge(d, how="outer", on="Base pair")

        return self.annotations_dataframe
    
    def write_annotations_to_csv(self, output_filename):
        self.annotations_dataframe.to_csv(output_filename)



        

