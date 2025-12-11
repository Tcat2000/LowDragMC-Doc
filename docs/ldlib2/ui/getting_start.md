# Getting Started
{{ version_badge("2.1.0", label="Since", icon="tag") }}

In this section, we will give you some examples step by step.

### Create a ModularUI

Let's use LDLib2 to create a simple UI. Basically, we need to create a `ModularUI`, which is a ui instance managerment during the runtime, and maintain the lifecycle, rendering, interaction of ui components you created. It accepts `UI` and `Player (Optional)` as inputs.

```java
private static ModularUI createModularUI() {
    
}
```

### Dislay ModularUI in your screen

Next step is to diaply our ui. Unlike most UI libraries which require you to use their specific screen. 
LDLib2 provides a universial soliution to render the interact with `ModularUI`. It can be used in any screen you want. 
Therefore, you can create and init a `ModularUI` during the init stage of a screen as below.

```java
@OnlyIn(Dist.CLIENT)
public class MyScreen extends Screen {
    // .....

    // initial
    @Override
    public void init() {
        super.init();
        var modularUI = createModularUI();
        modularUI.setScreenAndInit(this);
        this.addRenderableWidget(modularUI.getWidget());
    }

    // .....
}
```