---
date: 2026-09-24
rubric: tech
title_ru: Опенсорсный проект дал виртуальным машинам «настоящую» видеокарту Nvidia
title_en: An open-source project gives VMs a "real" Nvidia GPU, not an emulated one
dek_ru: virtio-nvgpu прокидывает GPU в гостевую систему KVM с потерей производительности около 2% — и позволяет делить одну карту между несколькими виртуалками.
dek_en: virtio-nvgpu passes a GPU into a KVM guest with roughly 2% overhead — and lets several VMs share one card cleanly.
source: https://github.com/nestrilabs/virtio-nvgpu
generated: true
---

## Русская версия

Компания Nestrilabs опубликовала в открытом доступе проект virtio-nvgpu — способ дать виртуальной машине под KVM практически полноценный доступ к видеокарте Nvidia, [говорится в описании репозитория на GitHub](https://github.com/nestrilabs/virtio-nvgpu). На RTX 3060 время рендеринга кадра в гостевой системе отличается от «голого железа» примерно на 2% — для решений с проброской GPU в виртуалки это близко к пределу возможного.

Технически проект не транслирует графическое API, как делают многие альтернативы, а перехватывает и пересылает между гостем и хостом вызовы ioctl — то есть команды, которые обычно идут напрямую к драйверу ядра Nvidia. Драйвер в гостевой системе сериализует запросы через virtqueue, а компонент на хосте превращает дескрипторы гостя в дескрипторы хоста и занимается трансляцией указателей и файловых дескрипторов. Как формулируют это сами авторы: «гостевая система запускает настоящие пользовательские драйверы Nvidia без изменений — те же библиотеки, тот же Vulkan и NVENC».

Отдельно авторы подчёркивают экономичность подхода по процессору: «гостевая система стоит ровно столько же, сколько стоил бы хост» — то есть накладные расходы на виртуализацию рендеринга практически не заметны. В тесте с четырьмя одновременными гостями, делящими одну карту, время отрисовки кадра (p50) у всех четырёх оказалось почти идентичным — 39,165, 39,164, 39,168 и 39,165 мс, что говорит о честном и предсказуемом распределении ресурсов GPU между виртуалками. Проект распространяется под разными лицензиями по компонентам: гостевой драйвер ядра — GPL-2.0, компонент устройства на хосте — Apache-2.0, общие протокольные описания — BSD-3-Clause или GPL-2.0+.

### Почему это важно

Для облачного гейминга, headless-стриминга и любых сценариев, где виртуалке нужен не эмулированный, а «настоящий» GPU, проброска на уровне ABI драйвера — принципиально другой уровень производительности по сравнению с трансляцией графических API. Открытая реализация с воспроизводимыми цифрами (а не маркетинговым «почти нативно») даёт инфраструктурным командам конкретный ориентир, чего вообще можно добиться от GPU-виртуализации сегодня.

## English version

Nestrilabs has open-sourced virtio-nvgpu, a way to give a KVM guest near-full access to an Nvidia GPU, [according to the project's GitHub repository](https://github.com/nestrilabs/virtio-nvgpu). On an RTX 3060, guest frame times come within about 2% of bare metal — close to the practical ceiling for GPU passthrough into virtual machines.

Technically, the project doesn't translate a graphics API the way many alternatives do. Instead it intercepts and forwards ioctl calls — the commands that normally go straight to Nvidia's kernel driver — between guest and host. The guest kernel driver serializes requests over a virtqueue, while a host-side device component maps the guest's handles to host descriptors and translates pointers and file descriptors. As the authors put it: "the guest runs NVIDIA's real user-mode drivers, unmodified — the same libraries, the same Vulkan and NVENC."

The authors also stress the CPU-side efficiency: "a guest costs what the host costs," meaning virtualization overhead for rendering is effectively negligible. In a test with four simultaneous guests sharing one GPU, p50 frame times across all four came out nearly identical — 39.165, 39.164, 39.168 and 39.165 ms — pointing to fair, predictable resource sharing rather than one guest starving the others. The project ships under a mix of licenses by component: GPL-2.0 for the guest kernel driver, Apache-2.0 for the host device crate, and BSD-3-Clause/GPL-2.0+ for the shared protocol definitions.

### Why it matters

For cloud gaming, headless streaming, and any setup where a VM needs a genuinely real GPU rather than an emulated one, ABI-level driver passthrough is a different performance tier from API translation. An open implementation with reproducible numbers — rather than marketing claims of "near-native" — gives infrastructure teams a concrete benchmark for what GPU virtualization can actually deliver today.
