from pydantic import BaseModel, Field


# class CurrentUser(BaseModel):
#     model_config = ConfigDict(validate_assignment=True)
#
#     id: int = Field(None, description="ID")


class CurrentUser(BaseModel):
    id: int = Field(None, description="ID")

    class Config:
        validate_assignment = True
