# Get Started

Creating UI using `Java` and `KubeJS` is mostly the same. This page will introduce the basic workflow of creating and using a UI.  

The entire **UI creation and usage pipeline** consists of the following steps:

1. Create UI widget and layout (1)
    { .annotate }

    1.  :material-hexagon-multiple: Create `buttons` and `item slots`, set their positions...

2. Bind UI functional logic (1)
    { .annotate }

    1.  :material-hexagon-multiple: Add logic to be executed when a `button` is clicked, bind `inventory` to `item slots`...

3. Display the UI (1)
    { .annotate }

    1.  :material-hexagon-multiple: Open the `GUI` when `right-clicking` an item, open the `GUI` when `right-clicking` a block...

---

Technically, the `UI function binding` and `UI widget creation` processes happen simultaneously, as many controls provide constructors that bind functions at the same time.  

On this page, we **separate step 1 and step 2** in the code examples to provide a clearer understanding of how the `UI` works.

## Create `UI` Widgets and Layout

Let's begin with a [`WigetGroup`](../widget/WidgetGroup.md), which is one of the mostly used widget. `WidgetGroup` is a container of child widgts. Therefore, we should create a `WidgetGroup` as 