# Layer 20 — Image Pipeline

Implementation commit: 733457c310d65ffbf3ccc4169662d485373beb6d
Implementation path: layers/layer20_image_pipeline

## Source inventory
- Python modules: **11**
- Classes: **13**
- Functions/methods: **49**

## Python modules
- layers/layer20_image_pipeline/__init__.py
- layers/layer20_image_pipeline/modules/batch_generator/__init__.py
- layers/layer20_image_pipeline/modules/batch_generator/batch_generator.py
- layers/layer20_image_pipeline/modules/composition_engine/__init__.py
- layers/layer20_image_pipeline/modules/composition_engine/composition_engine.py
- layers/layer20_image_pipeline/modules/prompt_builder/__init__.py
- layers/layer20_image_pipeline/modules/prompt_builder/prompt_builder.py
- layers/layer20_image_pipeline/modules/provider_router/__init__.py
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py
- layers/layer20_image_pipeline/modules/style_engine/__init__.py
- layers/layer20_image_pipeline/modules/style_engine/style_engine.py

## Classes
- layers/layer20_image_pipeline/modules/batch_generator/batch_generator.py:11 BatchStatus
- layers/layer20_image_pipeline/modules/batch_generator/batch_generator.py:18 BatchJob
- layers/layer20_image_pipeline/modules/batch_generator/batch_generator.py:52 BatchGenerator
- layers/layer20_image_pipeline/modules/composition_engine/composition_engine.py:8 CompositionRule
- layers/layer20_image_pipeline/modules/composition_engine/composition_engine.py:20 CompositionPlan
- layers/layer20_image_pipeline/modules/composition_engine/composition_engine.py:88 CompositionEngine
- layers/layer20_image_pipeline/modules/prompt_builder/prompt_builder.py:8 ImagePrompt
- layers/layer20_image_pipeline/modules/prompt_builder/prompt_builder.py:40 PromptBuilder
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py:10 ProviderStatus
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py:17 ImageProvider
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py:56 ProviderRouter
- layers/layer20_image_pipeline/modules/style_engine/style_engine.py:7 StylePreset
- layers/layer20_image_pipeline/modules/style_engine/style_engine.py:34 StyleEngine

## Functions / methods
- layers/layer20_image_pipeline/modules/batch_generator/batch_generator.py:30 __init__()
- layers/layer20_image_pipeline/modules/batch_generator/batch_generator.py:40 to_dict()
- layers/layer20_image_pipeline/modules/batch_generator/batch_generator.py:53 __init__()
- layers/layer20_image_pipeline/modules/batch_generator/batch_generator.py:58 set_generator()
- layers/layer20_image_pipeline/modules/batch_generator/batch_generator.py:64 create_batch()
- layers/layer20_image_pipeline/modules/batch_generator/batch_generator.py:74 execute_batch()
- layers/layer20_image_pipeline/modules/batch_generator/batch_generator.py:120 get_batch()
- layers/layer20_image_pipeline/modules/batch_generator/batch_generator.py:124 list_batches()
- layers/layer20_image_pipeline/modules/composition_engine/composition_engine.py:11 __init__()
- layers/layer20_image_pipeline/modules/composition_engine/composition_engine.py:23 __init__()
- layers/layer20_image_pipeline/modules/composition_engine/composition_engine.py:47 add_element()
- layers/layer20_image_pipeline/modules/composition_engine/composition_engine.py:79 to_dict()
- layers/layer20_image_pipeline/modules/composition_engine/composition_engine.py:89 __init__()
- layers/layer20_image_pipeline/modules/composition_engine/composition_engine.py:98 create_plan()
- layers/layer20_image_pipeline/modules/composition_engine/composition_engine.py:109 add_layout()
- layers/layer20_image_pipeline/modules/composition_engine/composition_engine.py:116 add_rule()
- layers/layer20_image_pipeline/modules/composition_engine/composition_engine.py:121 validate()
- layers/layer20_image_pipeline/modules/composition_engine/composition_engine.py:148 list_layouts()
- layers/layer20_image_pipeline/modules/prompt_builder/prompt_builder.py:19 __init__()
- layers/layer20_image_pipeline/modules/prompt_builder/prompt_builder.py:28 to_dict()
- layers/layer20_image_pipeline/modules/prompt_builder/prompt_builder.py:41 __init__()
- layers/layer20_image_pipeline/modules/prompt_builder/prompt_builder.py:50 build()
- layers/layer20_image_pipeline/modules/prompt_builder/prompt_builder.py:78 add_template()
- layers/layer20_image_pipeline/modules/prompt_builder/prompt_builder.py:85 add_style()
- layers/layer20_image_pipeline/modules/prompt_builder/prompt_builder.py:92 from_template()
- layers/layer20_image_pipeline/modules/prompt_builder/prompt_builder.py:101 optimize_for_platform()
- layers/layer20_image_pipeline/modules/prompt_builder/prompt_builder.py:122 list_styles()
- layers/layer20_image_pipeline/modules/prompt_builder/prompt_builder.py:125 list_templates()
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py:28 __init__()
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py:46 to_dict()
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py:57 __init__()
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py:62 register()
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py:73 unregister()
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py:77 route()
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py:150 record_observation()
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py:172 list_providers()
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py:176 get_provider()
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py:180 set_status()
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py:190 history()
- layers/layer20_image_pipeline/modules/style_engine/style_engine.py:10 __init__()
- layers/layer20_image_pipeline/modules/style_engine/style_engine.py:25 to_dict()
- layers/layer20_image_pipeline/modules/style_engine/style_engine.py:35 __init__()
- layers/layer20_image_pipeline/modules/style_engine/style_engine.py:39 add_preset()
- layers/layer20_image_pipeline/modules/style_engine/style_engine.py:44 get_preset()
- layers/layer20_image_pipeline/modules/style_engine/style_engine.py:47 set_brand_style()
- layers/layer20_image_pipeline/modules/style_engine/style_engine.py:52 get_brand_style()
- layers/layer20_image_pipeline/modules/style_engine/style_engine.py:55 apply_style()
- layers/layer20_image_pipeline/modules/style_engine/style_engine.py:68 list_presets()
- layers/layer20_image_pipeline/modules/style_engine/style_engine.py:71 suggest_style()

## Status discipline
Generated from the implementation tree. Source presence is not live-provider or production-runtime certification.
