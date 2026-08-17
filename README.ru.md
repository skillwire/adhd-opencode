# adhd-style — стиль вывода для opencode от SkillWire

![License: AGPL-3.0](https://img.shields.io/badge/license-AGPL--3.0-blue.svg)
![Install](https://img.shields.io/badge/install-npx%20skills%20add%20skillwire%2Fadhd--opencode-lightgrey)
![Release](https://img.shields.io/github/v/release/skillwire/adhd-opencode)

Стиль вывода, дружелюбный к СДВГ-читателю: ответ-действие первым, нумерованные шаги, конкретные следующие шаги, оценки времени, без преамбул. Диагноз не нужен — стиль меняет то, как агент *говорит*, а не что он делает.

Этот репозиторий — **каталог стилей вывода** для кодинг-агентов от SkillWire: `adhd-style` — первый из них; новые стили будут появляться в `skills/<name>/`. Имя репо (`adhd-opencode`) и имя скилла (`adhd-style`) намеренно независимы: `npx skills add` привязывает установки и обновления к `name` скилла, а не к репо.

Проверено боем: набор правил прошёл шесть независимых red-team-аудитов против механизмов плагин/скилл/гейт opencode и с каждым раундом становился проще.

## Зачем это

- **Ответ первым.** Первая строка — суть, команда, путь. Кто прочитает только её — уже получит ответ.
- **Коротко по умолчанию.** Скажи минимум, который полностью отвечает, и остановись. Вода тратит внимание впустую.
- **Сканируемость.** Одна мысль на блок `**→**`, жирное несёт весь ответ, пустые строки между пунктами.
- **Числа священны.** Указывай пороги точно; не расширяй «только X» до «все»; предупреждение едет с тем, что оно защищает.
- **Нет фальшивого off.** Исключения безопасности (подтверждение деструктивных действий, debug-спираль, неоднозначность) всегда включены, даже в «кратком» режиме.

## До / после

Тот же вопрос — *«как ускорить сборку TypeScript?»* — без стиля и со стилем.

| Обычно | adhd-style |
|---|---|
| Абзац, который начинается с контекста, перечисляет возможности, прячет рекомендацию и заканчивается «надеюсь, поможет» | `**→ Run npx tsc --noEmit and fix what it names.**` затем нумерованные 1-2-3, оговорка и один следующий шаг. |

Измерено на исходном стиле: работа не меняется (97%/97% hidden tests), вывод ~43% короче, ответ в первой строке в 75% случаев против 3%. (Self-reported бенчмарк upstream; воспроизводится в [attention-span](https://github.com/alexgreensh/attention-span).)

## Совместимость

Тело стиля — обычный markdown без харнесс-специфичного синтаксиса, его можно положить в rules-файл любого агента.

| Харнесс | Always-on (rules-файл) | По запросу (скилл) | Примечания |
|---|---|---|---|
| opencode | ✅ `instructions` / AGENTS.md | ✅ skill-тул | Перечитывается каждый ход, переживает компакцию, действует и на сабагентов |
| Claude Code | ✅ `CLAUDE.md` / `output-styles` | ✅ скилл | Frontmatter срезается; тело чистое |
| Codex / AGENTS.md | ✅ добавить в `AGENTS.md` | — | Чистое markdown-тело |
| Gemini CLI | ✅ `GEMINI.md` | — | Чистое markdown-тело |

> Always-on — надёжный путь (документированный trade-off в [INSTALL](INSTALL.md)); on-demand-скилл может «дрейфовать» на длинных сессиях.

## Установка (opencode)

### Always-on (рекомендуется) — переживает компакцию, перечитывается каждый ход

```bash
mkdir -p ~/.config/opencode
cp skills/adhd-style/output-style.md ~/.config/opencode/output-style.md
```

Затем добавить в `~/.config/opencode/opencode.jsonc`:

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": ["~/.config/opencode/output-style.md"]
}
```

Перезапустить opencode. Готово — каждая сессия, каждый сабагент, переживает компакцию.

### По запросу (skill-тул / npx skills)

```bash
npx skills add skillwire/adhd-opencode          # последняя версия
npx skills add skillwire/adhd-opencode@v0.1     # закрепить релиз
```

Затем загрузить через `skill`-тул или создать команду:

```markdown
# ~/.config/opencode/commands/adhd-style.md
Use the `adhd-style` skill and apply its ruleset for the rest of this session.
```

> Загрузка по запросу действует только на текущую сессию; на длинных сессиях правила могут дрейфовать — для постоянного дефолта используйте always-on.

## Содержимое

| Файл | Что это |
|---|---|
| `skills/adhd-style/SKILL.md` | Скилл (frontmatter + полный ruleset) для skill-тула / `npx skills` |
| `skills/adhd-style/output-style.md` | Тело стиля без frontmatter — единый источник; кладётся в `instructions` для always-on |
| `install/opencode.jsonc.example` | Минимальный пример конфига |

## Кастомизация

Стиль — обычное markdown-тело. Форкните, правьте `skills/adhd-style/output-style.md`, храните свою копию. Ноль зависимостей.

## Лицензия и атрибуция

**AGPL-3.0.** Репозиторий — сжатая производная от стиля *Attention-kind* из [attention-span](https://github.com/alexgreensh/attention-span) (AGPL-3.0) вперемешку с правилами из [i-have-adhd](https://github.com/ayghri/i-have-adhd) (MIT). См. [NOTICE](NOTICE) и [LICENSE](LICENSE). Соответствие лицензиям объявлено через SPDX по спецификации REUSE (см. `REUSE.toml`); проверить — `reuse lint`.

Для личного использования в своём конфиге ничего дополнительно не требуется. При распространении модификаций действует AGPL share-alike.
