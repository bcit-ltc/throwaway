import dagger
from dagger import dag, function, object_type, Container, DefaultPath, Directory, Secret, Doc, Enum, EnvVariable, enum_type
from typing import Annotated
# import asyncio
import json

@enum_type
class Environment(Enum):
    STABLE = "stable"
    REVIEW = "review"
    LATEST = "latest"
    LOCAL = "local"
    NONE = "none"

MAIN_BRANCH = "main"

@object_type
class Throwaway: # this will be our pipeline-manager module

    @function
    async def run(self,
                source: Annotated[Directory, Doc("Source directory"), DefaultPath(".")], # source directory
                  ) -> str:

        print(dir(dag.pipeline_manager))

        

        return await dag.pipeline_manager().run()

