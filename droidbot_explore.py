import subprocess


def run_droidbot(apk_path: str, exploration_time: int, output_dir: str) -> None:

    droid_command: str = (
        f"droidbot -a {apk_path} -is_emulator -keep_app -grant_perm -timeout {exploration_time} -o {output_dir}"
    )
    print(f"Executing command: {droid_command}")
    process = subprocess.run(droid_command, shell=True, capture_output=True, text=True)

    print("STDOUT:", process.stdout)
    print("STDERR:", process.stderr)

    print("Finished running droidbot")
