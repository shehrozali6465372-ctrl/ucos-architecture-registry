# Layer 21 — Deployment

Implementation commit: 9836a8f782cde59c4f8e3608b1fb16031076f38f
Implementation path: layers/layer21_deployment

## Source inventory
- Python modules: **12**
- Classes: **20**
- Functions/methods: **65**

## Python modules
- layers/layer21_deployment/__init__.py
- layers/layer21_deployment/modules/build_manager/__init__.py
- layers/layer21_deployment/modules/build_manager/build_manager.py
- layers/layer21_deployment/modules/docker_engine/__init__.py
- layers/layer21_deployment/modules/docker_engine/docker_deployment_manager.py
- layers/layer21_deployment/modules/docker_engine/docker_engine.py
- layers/layer21_deployment/modules/environment_manager/__init__.py
- layers/layer21_deployment/modules/environment_manager/environment_manager.py
- layers/layer21_deployment/modules/release_manager/__init__.py
- layers/layer21_deployment/modules/release_manager/release_manager.py
- layers/layer21_deployment/modules/startup_manager/__init__.py
- layers/layer21_deployment/modules/startup_manager/startup_manager.py

## Classes
- layers/layer21_deployment/modules/build_manager/build_manager.py:9 BuildStatus
- layers/layer21_deployment/modules/build_manager/build_manager.py:13 BuildStep
- layers/layer21_deployment/modules/build_manager/build_manager.py:24 Build
- layers/layer21_deployment/modules/build_manager/build_manager.py:42 BuildManager
- layers/layer21_deployment/modules/docker_engine/docker_deployment_manager.py:12 ContainerHealth
- layers/layer21_deployment/modules/docker_engine/docker_deployment_manager.py:37 DeploymentConfig
- layers/layer21_deployment/modules/docker_engine/docker_deployment_manager.py:76 DeploymentStatus
- layers/layer21_deployment/modules/docker_engine/docker_deployment_manager.py:101 DockerDeploymentManager
- layers/layer21_deployment/modules/docker_engine/docker_engine.py:6 DockerConfig
- layers/layer21_deployment/modules/docker_engine/docker_engine.py:35 DockerCompose
- layers/layer21_deployment/modules/docker_engine/docker_engine.py:56 DockerEngine
- layers/layer21_deployment/modules/environment_manager/environment_manager.py:8 Environment
- layers/layer21_deployment/modules/environment_manager/environment_manager.py:12 EnvironmentConfig
- layers/layer21_deployment/modules/environment_manager/environment_manager.py:27 EnvironmentManager
- layers/layer21_deployment/modules/release_manager/release_manager.py:9 ReleaseStatus
- layers/layer21_deployment/modules/release_manager/release_manager.py:13 Release
- layers/layer21_deployment/modules/release_manager/release_manager.py:33 ReleaseManager
- layers/layer21_deployment/modules/startup_manager/startup_manager.py:8 StartupPhase
- layers/layer21_deployment/modules/startup_manager/startup_manager.py:12 StartupStep
- layers/layer21_deployment/modules/startup_manager/startup_manager.py:25 StartupManager

## Functions / methods
- layers/layer21_deployment/modules/build_manager/build_manager.py:16 __init__()
- layers/layer21_deployment/modules/build_manager/build_manager.py:28 __init__()
- layers/layer21_deployment/modules/build_manager/build_manager.py:37 to_dict()
- layers/layer21_deployment/modules/build_manager/build_manager.py:43 __init__()
- layers/layer21_deployment/modules/build_manager/build_manager.py:47 create_build()
- layers/layer21_deployment/modules/build_manager/build_manager.py:54 execute_build()
- layers/layer21_deployment/modules/build_manager/build_manager.py:68 get_build()
- layers/layer21_deployment/modules/build_manager/build_manager.py:71 list_builds()
- layers/layer21_deployment/modules/docker_engine/docker_deployment_manager.py:326 get_docker_manager()
- layers/layer21_deployment/modules/docker_engine/docker_deployment_manager.py:15 __init__()
- layers/layer21_deployment/modules/docker_engine/docker_deployment_manager.py:25 to_dict()
- layers/layer21_deployment/modules/docker_engine/docker_deployment_manager.py:40 __init__()
- layers/layer21_deployment/modules/docker_engine/docker_deployment_manager.py:48 add_service()
- layers/layer21_deployment/modules/docker_engine/docker_deployment_manager.py:66 to_dict()
- layers/layer21_deployment/modules/docker_engine/docker_deployment_manager.py:80 __init__()
- layers/layer21_deployment/modules/docker_engine/docker_deployment_manager.py:89 to_dict()
- layers/layer21_deployment/modules/docker_engine/docker_deployment_manager.py:108 __new__()
- layers/layer21_deployment/modules/docker_engine/docker_deployment_manager.py:116 __init__()
- layers/layer21_deployment/modules/docker_engine/docker_deployment_manager.py:125 _setup_default_config()
- layers/layer21_deployment/modules/docker_engine/docker_deployment_manager.py:151 _run_command()
- layers/layer21_deployment/modules/docker_engine/docker_deployment_manager.py:163 check_docker_available()
- layers/layer21_deployment/modules/docker_engine/docker_deployment_manager.py:181 get_container_health()
- layers/layer21_deployment/modules/docker_engine/docker_deployment_manager.py:217 check_all_containers()
- layers/layer21_deployment/modules/docker_engine/docker_deployment_manager.py:233 deploy()
- layers/layer21_deployment/modules/docker_engine/docker_deployment_manager.py:256 stop()
- layers/layer21_deployment/modules/docker_engine/docker_deployment_manager.py:260 restart()
- layers/layer21_deployment/modules/docker_engine/docker_deployment_manager.py:267 get_logs()
- layers/layer21_deployment/modules/docker_engine/docker_deployment_manager.py:271 get_deployment_status()
- layers/layer21_deployment/modules/docker_engine/docker_deployment_manager.py:283 verify_deployment()
- layers/layer21_deployment/modules/docker_engine/docker_engine.py:10 __init__()
- layers/layer21_deployment/modules/docker_engine/docker_engine.py:21 to_dict()
- layers/layer21_deployment/modules/docker_engine/docker_engine.py:25 generate_dockerfile()
- layers/layer21_deployment/modules/docker_engine/docker_engine.py:36 __init__()
- layers/layer21_deployment/modules/docker_engine/docker_engine.py:40 add_service()
- layers/layer21_deployment/modules/docker_engine/docker_engine.py:43 generate()
- layers/layer21_deployment/modules/docker_engine/docker_engine.py:57 __init__()
- layers/layer21_deployment/modules/docker_engine/docker_engine.py:61 create_config()
- layers/layer21_deployment/modules/docker_engine/docker_engine.py:67 get_config()
- layers/layer21_deployment/modules/docker_engine/docker_engine.py:70 generate_compose()
- layers/layer21_deployment/modules/docker_engine/docker_engine.py:73 generate_dockerfile()
- layers/layer21_deployment/modules/docker_engine/docker_engine.py:77 list_configs()
- layers/layer21_deployment/modules/environment_manager/environment_manager.py:15 __init__()
- layers/layer21_deployment/modules/environment_manager/environment_manager.py:22 to_dict()
- layers/layer21_deployment/modules/environment_manager/environment_manager.py:28 __init__()
- layers/layer21_deployment/modules/environment_manager/environment_manager.py:32 create()
- layers/layer21_deployment/modules/environment_manager/environment_manager.py:37 set_variable()
- layers/layer21_deployment/modules/environment_manager/environment_manager.py:44 get_variable()
- layers/layer21_deployment/modules/environment_manager/environment_manager.py:48 activate()
- layers/layer21_deployment/modules/environment_manager/environment_manager.py:58 get_current()
- layers/layer21_deployment/modules/environment_manager/environment_manager.py:61 list_environments()
- layers/layer21_deployment/modules/release_manager/release_manager.py:17 __init__()
- layers/layer21_deployment/modules/release_manager/release_manager.py:27 to_dict()
- layers/layer21_deployment/modules/release_manager/release_manager.py:34 __init__()
- layers/layer21_deployment/modules/release_manager/release_manager.py:38 create_release()
- layers/layer21_deployment/modules/release_manager/release_manager.py:43 add_change()
- layers/layer21_deployment/modules/release_manager/release_manager.py:50 release()
- layers/layer21_deployment/modules/release_manager/release_manager.py:59 rollback()
- layers/layer21_deployment/modules/release_manager/release_manager.py:66 get_current_version()
- layers/layer21_deployment/modules/release_manager/release_manager.py:69 list_releases()
- layers/layer21_deployment/modules/startup_manager/startup_manager.py:15 __init__()
- layers/layer21_deployment/modules/startup_manager/startup_manager.py:26 __init__()
- layers/layer21_deployment/modules/startup_manager/startup_manager.py:30 add_step()
- layers/layer21_deployment/modules/startup_manager/startup_manager.py:36 startup()
- layers/layer21_deployment/modules/startup_manager/startup_manager.py:54 list_steps()
- layers/layer21_deployment/modules/startup_manager/startup_manager.py:58 get_history()

## Status discipline
Generated from the implementation tree. Source presence is not live-provider or production-runtime certification.
