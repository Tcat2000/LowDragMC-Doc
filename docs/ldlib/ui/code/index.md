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

Technically, the `UI function binding` and `UI widget creation` processes happen simultaneously, as many controls provide constructors that bind functions at the same time.  

On this page, we **separate step 1 and step 2** in the code examples to provide a clearer understanding of how the `UI` works.

---

## Create `UI` Widgets and Layout
    
Let's begin with a [`WigetGroup`](../widget/WidgetGroup.md), which is a container of child widgtes. Therefore, we create a `WidgetGroup` as a root widget. 

Then, we add a `Label` and a `Button` into it.

=== "Java"

    ``` java 
    public WidgetGroup createUI() {
        // create a root container
        var root = new WidgetGroup();
        root.setSize(100, 100);
        root.setBackground(ResourceBorderTexture.BORDERED_BACKGROUND);

        // create a label and a button
        var label = new LabelWidget();
        label.setSelfPosition(20, 20);
        label.setText("Hello, World!");
        var button = new ButtonWidget();
        button.setSelfPosition(20, 100);
        button.setSize(60, 20);
        button.setButtonTexture(ResourceBorderTexture.BUTTON_COMMON, new TextTexture("Click me!"));
        button.setHoverTexture(ResourceBorderTexture.BUTTON_COMMON.copy().setColor(ColorPattern.CYAN.color), new TextTexture("Click me!"));

        // add the label and button to the root container
        root.addWidgets(label, button);
        return root;
    }
    ```

=== "KubeJS"

    ``` javascript
    function createUI() {
        // create a root container
        let root = new WidgetGroup();
        root.setSize(100, 100);
        root.setBackground(ResourceBorderTexture.BORDERED_BACKGROUND);

        // create a label and a button
        let label = new LabelWidget();
        label.setSelfPosition(20, 20);
        label.setText("Hello, World!");
        let button = new ButtonWidget();
        button.setSelfPosition(20, 60);
        button.setSize(60, 20);
        button.setButtonTexture(ResourceBorderTexture.BUTTON_COMMON, new TextTexture("Click me!"));
        button.setHoverTexture(ResourceBorderTexture.BUTTON_COMMON.copy().setColor(ColorPattern.CYAN.color), new TextTexture("Click me!"));

        // add the label and button to the root container
        root.addWidgets(label, button);
        return root;
    }
    ```
    
 ![Image title](../images/root.png){ width="80%" style="display: block; margin: 0 auto;" }

---



