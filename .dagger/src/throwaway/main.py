import dagger
from dagger import dag, function, object_type, Container, DefaultPath, Directory, Secret, Doc, Enum, EnvVariable, enum_type
from typing import Annotated

@object_type
class Throwaway: # this will be our pipeline-manager module

    @function
    async def run(self,
                source: Annotated[Directory, Doc("Source directory"), DefaultPath(".")], # source directory
                github_token: Annotated[Secret, Doc("Github Token")] | None,
                username: Annotated[str, Doc("Github Username")] | None,  # GitHub username
                branch: Annotated[str, Doc("Current Branch")] | None,  # Current branch
                commit_hash: Annotated[str, Doc("Current Commit Hash")] | None,  # Current commit hash
                ) -> str:

        print(dir(dag.pipeline_manager()))

        
        return await dag.pipeline_manager().run(
            source=source,
            github_token=github_token,
            username=username,
            branch=branch,
            commit_hash=commit_hash
        )

