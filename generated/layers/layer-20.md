# Layer 20 — Image Pipeline

Implementation commit: 69b56124c22a339be67e260c1a568d189962481e
Implementation path: layers/layer20_image_pipeline

## Source inventory
- Python modules: **11**
- Classes: **13**
- Functions/methods: **48**

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
- layers/layer20_image_pipeline/modules/batch_generator/batch_generator.py:9 BatchStatus
- layers/layer20_image_pipeline/modules/batch_generator/batch_generator.py:13 BatchJob
- layers/layer20_image_pipeline/modules/batch_generator/batch_generator.py:33 BatchGenerator
- layers/layer20_image_pipeline/modules/composition_engine/composition_engine.py:6 CompositionRule
- layers/layer20_image_pipeline/modules/composition_engine/composition_engine.py:16 CompositionPlan
- layers/layer20_image_pipeline/modules/composition_engine/composition_engine.py:35 CompositionEngine
- layers/layer20_image_pipeline/modules/prompt_builder/prompt_builder.py:6 ImagePrompt
- layers/layer20_image_pipeline/modules/prompt_builder/prompt_builder.py:25 PromptBuilder
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py:8 ProviderStatus
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py:12 ImageProvider
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py:31 ProviderRouter
- layers/layer20_image_pipeline/modules/style_engine/style_engine.py:6 StylePreset
- layers/layer20_image_pipeline/modules/style_engine/style_engine.py:23 StyleEngine

## Functions / methods
- layers/layer20_image_pipeline/modules/batch_generator/batch_generator.py:17 __init__()
- layers/layer20_image_pipeline/modules/batch_generator/batch_generator.py:27 to_dict()
- layers/layer20_image_pipeline/modules/batch_generator/batch_generator.py:34 __init__()
- layers/layer20_image_pipeline/modules/batch_generator/batch_generator.py:38 set_generator()
- layers/layer20_image_pipeline/modules/batch_generator/batch_generator.py:41 create_batch()
- layers/layer20_image_pipeline/modules/batch_generator/batch_generator.py:46 execute_batch()
- layers/layer20_image_pipeline/modules/batch_generator/batch_generator.py:64 get_batch()
- layers/layer20_image_pipeline/modules/batch_generator/batch_generator.py:67 list_batches()
- layers/layer20_image_pipeline/modules/composition_engine/composition_engine.py:9 __init__()
- layers/layer20_image_pipeline/modules/composition_engine/composition_engine.py:19 __init__()
- layers/layer20_image_pipeline/modules/composition_engine/composition_engine.py:26 add_element()
- layers/layer20_image_pipeline/modules/composition_engine/composition_engine.py:30 to_dict()
- layers/layer20_image_pipeline/modules/composition_engine/composition_engine.py:36 __init__()
- layers/layer20_image_pipeline/modules/composition_engine/composition_engine.py:45 create_plan()
- layers/layer20_image_pipeline/modules/composition_engine/composition_engine.py:52 add_layout()
- layers/layer20_image_pipeline/modules/composition_engine/composition_engine.py:55 add_rule()
- layers/layer20_image_pipeline/modules/composition_engine/composition_engine.py:58 validate()
- layers/layer20_image_pipeline/modules/composition_engine/composition_engine.py:65 list_layouts()
- layers/layer20_image_pipeline/modules/prompt_builder/prompt_builder.py:10 __init__()
- layers/layer20_image_pipeline/modules/prompt_builder/prompt_builder.py:19 to_dict()
- layers/layer20_image_pipeline/modules/prompt_builder/prompt_builder.py:26 __init__()
- layers/layer20_image_pipeline/modules/prompt_builder/prompt_builder.py:35 build()
- layers/layer20_image_pipeline/modules/prompt_builder/prompt_builder.py:47 add_template()
- layers/layer20_image_pipeline/modules/prompt_builder/prompt_builder.py:50 add_style()
- layers/layer20_image_pipeline/modules/prompt_builder/prompt_builder.py:53 from_template()
- layers/layer20_image_pipeline/modules/prompt_builder/prompt_builder.py:58 optimize_for_platform()
- layers/layer20_image_pipeline/modules/prompt_builder/prompt_builder.py:70 list_styles()
- layers/layer20_image_pipeline/modules/prompt_builder/prompt_builder.py:73 list_templates()
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py:16 __init__()
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py:26 to_dict()
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py:32 __init__()
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py:36 register()
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py:42 unregister()
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py:48 route()
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py:78 record_observation()
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py:88 list_providers()
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py:91 get_provider()
- layers/layer20_image_pipeline/modules/provider_router/provider_router.py:94 set_status()
- layers/layer20_image_pipeline/modules/style_engine/style_engine.py:9 __init__()
- layers/layer20_image_pipeline/modules/style_engine/style_engine.py:18 to_dict()
- layers/layer20_image_pipeline/modules/style_engine/style_engine.py:24 __init__()
- layers/layer20_image_pipeline/modules/style_engine/style_engine.py:28 add_preset()
- layers/layer20_image_pipeline/modules/style_engine/style_engine.py:31 get_preset()
- layers/layer20_image_pipeline/modules/style_engine/style_engine.py:34 set_brand_style()
- layers/layer20_image_pipeline/modules/style_engine/style_engine.py:37 get_brand_style()
- layers/layer20_image_pipeline/modules/style_engine/style_engine.py:40 apply_style()
- layers/layer20_image_pipeline/modules/style_engine/style_engine.py:48 list_presets()
- layers/layer20_image_pipeline/modules/style_engine/style_engine.py:51 suggest_style()

## Status discipline
Generated from the implementation tree. Source presence is not live-provider or production-runtime certification.
