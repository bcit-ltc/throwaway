import dagger
from dagger import dag, function, object_type, Container, DefaultPath
from typing import Annotated
import asyncio

@object_type
class Throwaway: # this will be our pipeline-manager module
    
    
    @function
    async def publish(self) -> None:
        print("Publishing...")
        tag = await self.create_tag()
        container = await self.build_image()

        return await container.publish(
            f"some_registry/some_repo:{tag}"
        )

    @function
    def build_image(self,
            source: Annotated[
            dagger.Directory,
            DefaultPath("./")
        ],
        ) -> Container:

        self.run_tests()
        """Builds the image for the build"""
        return source.docker_build()

    @function
    async def run_tests(self) -> None:
        """Returns a container that echoes whatever string argument is provided"""
        return None

    @function
    async def create_tag(self) -> None:
        """Creates the tag for the build"""

        version_task = self.semantic_release()
        environment_task = self.determine_environment()

        version, environment = await asyncio.gather(version_task, environment_task)

        some_format_we_agreed_on = f"{version}-{environment}"

        return some_format_we_agreed_on

    
    @function
    def semantic_release(self) -> None:
        """Returns a container that echoes whatever string argument is provided"""
        return None
    
    @function
    def determine_environment(self) -> None:
        """Returns a container that echoes whatever string argument is provided"""
        return None