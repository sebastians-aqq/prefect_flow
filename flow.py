from prefect import flow

@flow(log_prints=True)
def find_wifi(name: str = "Spring"):
    print(f"Wifi {name}!")
    print(f"G2 ON!")
    print(f"G5 ON!")

if __name__ == "__main__":
    find_wifi()
