# December 2025

### Pull #14 [weilinfox/ruyi-litester#14](https://github.com/weilinfox/ruyi-litester/pull/14)
- Add testing for multiple Linux distributions under the ARM64 architecture
	- Utilize the arm64 native runner for workflow execution
### Pull #15 [weilinfox/ruyi-litester#15](https://github.com/weilinfox/ruyi-litester/pull/15)
- Add testing for multiple Linux distributions under the RISCV64 architecture
	- Configured QEMU to support riscv64 image building on the x86 architecture runner
### Pull #16 [weilinfox/ruyi-litester#16](https://github.com/weilinfox/ruyi-litester/pull/16)
- Fixed the issue where the ping command was not present
	- Used /dev/tcp to replace the ping command in the code to bypass the issue of ICMP protocol being prohibited in Github Actions
### Completed a test report for the RuyiSDK VSCode Extension [Test Report](https://github.com/YXCZS/plct_working/tree/main/December_2015/ruyisdk-vscode-extension-0.1.0-beta.1)
- Covered core extension features: package management, virtual environment management, news feed, etc.
