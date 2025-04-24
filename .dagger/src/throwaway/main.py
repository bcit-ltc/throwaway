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
    environment = Environment.NONE
    semantic_release_result = None

    @function
    async def run(self,
                source: Annotated[Directory, Doc("Source directory"), DefaultPath(".")], # source directory
                github_token: Annotated[Secret, Doc("Github Token")] | None,
                username: Annotated[str, Doc("Github Username")] | None,  # GitHub username
                branch: Annotated[str, Doc("Current Branch")] | None,  # Current branch
                commit_hash: Annotated[str, Doc("Current Commit Hash")] | None,  # Current commit hash
                  ) -> str:

        # Check for GitHub token
        if github_token is None:
            environment = Environment.LOCAL
        else:
            if branch == MAIN_BRANCH:
                # semantic_release = await self.semantic_release()
                semantic_release_result = '{ "next_release": null, "last_release": "1.0.1"}'

                # Convert JSON String to Python
                semantic_release_result = json.loads(semantic_release_result)
                print(semantic_release_result['next_release'])

                if semantic_release_result['next_release']:
                    environment = Environment.STABLE
                else:
                    environment = Environment.LATEST
            else:
                environment = Environment.REVIEW
    
        return environment

