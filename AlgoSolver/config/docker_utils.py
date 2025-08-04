async def start_docker_container(docker):
    print("Starting Docker conatiner....")
    await docker.start()

async def stop_docker_container(docker):
    print("Stopping Docker conatiner...")
    await docker.stop()
    print("Docker conatainer stopped. ")
    