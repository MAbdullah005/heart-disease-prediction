from pydantic import BaseModel,Field
from typing import Annotated,Dict

class predicationresponce(BaseModel):

    predication_categorey:str=Field(...,description='Predication of Heart deisease',
                                    examples=['NO','Yes'])
    
    confidence:float=Field(...,description='model Confidnce score for predication class ',
                           examples=[12.12])
    
    classes_probabilties:dict[str,float]=Field(...,description="probalities distribution across all ' \
                                             'possiable given classes",
                                             examples=[{'Low':0.01,'high':0.89}])