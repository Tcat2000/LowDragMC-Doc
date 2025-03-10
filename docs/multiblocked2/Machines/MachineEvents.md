#Machine Events

Machine Events are events that all called when at various times when things in the machine change, like a state, or a recipe starts or stops.<br>
Machine Events can be listened to in 2 ways, with the builtin node graph, or with external KubeJS scripts. Both will be covered here

# Machine Event List

### On Recipe Working Event
Runs every tick when the machine is processing a recipe.

### MachineEvents.MachineUIEvent
unsure, seems to be wip

### On Custom Data Update Event (Client)
Runs on the client when it receives an update to the custom NBT data.

### Machine Tick Event
Runs every game tick.

### Machine Client Tick Event
Runs every game tick on the client.

### After Recipe Working Event
Runs after a recipe processing stops.

### Recipe Status Changed Event
Runs any time a recipes status changes, i.e. working -> suspend.

### Before Recipe Working Event
Runs before a recipe starts, can be used to prevent a recipe from running, or add modifiers based on custom logic.

### State Changed Event
Runs when the machine state changes, i.e. base -> working. Machine state /= Recipe state.

### Drops Event
Runs when the machine is broken, can be used to change the drop or add custom logic to the saved NBT.

### Instruction Keyframe Event (pending PR)
Called on the client whenever a geckolib animation is playing, and an instruction keyframe is called.

### Placed Event
Called on machine place.

### On Load Event
Runs when the machine is loaded, chunk entering simulation distance, or world loaded in (within range).

### Remove Event
Called when the machine is broken or removed by commands.

### On Recipe Waiting Event
Runs every tick while the recipe is waiting.

### Fuel Recipe Modify Event
Allows modification or cancellation of fuel recipes.

### Right Click Event
Runs when the machine is clicked on.

### Open UI Event
Allows you to cansel the opening of the UI based on custom logic.

### Neighbor Changed Event
Runs when an adjacent block is changed.

### Before Recipe Modify Event
Allows canceling of recipe modification based on custom logic.

### Fuel Burning Finish Event
Runs when fuel recipe finishes.

### After Recipe Modify Event
Allows adding a hard cap to recipe modifications.

## Multiblock Machine Events

### Multiblock Structure Invalid Event
Triggers when the structure is invalid (evey time it changes?).

### Multiblock Structure Formed Event
Triggers when the structure forms.

### Multiblock Use Catalyst Event
Triggered before the structure is formed by a catalyst is used on the controller. Allows custom catalyst detection logic.

# The Node Graph

[wip]

# KubeJS Event Listening

Listening to machine events happens in ServerScripts.<br>
To listen for an event, use `MBDMachineEvents.<event name>("<machine id>", event => {<your code>});`
<br><br>
Example of a script to spawn particles on Instruction Keyframe Event
```java
MBDMachineEvents.onCustomKeyframeTrigger("mbd2:su_out", event => {
    var level = event.getEvent().getMachine().getLevel();
    var pos = event.getEvent().getMachine().pos;
    var machine = event.getEvent().getMachine();
    if(machine.getFrontFacing().get() == Direction.NORTH || machine.getFrontFacing().get() == Direction.SOUTH) {
        level.runCommandSilent("summon embers:ember_packet " + (pos.x + 0.7) + " " + (pos.y - 0.5) + " " + (pos.z + 0.5) + " {lifetime:15, destX:" + (pos.x + 1.7) + ",destY:" + (pos.y + 1) + ",destZ:" + (pos.z + 0.5) + ",value:0}")
        level.runCommandSilent("summon embers:ember_packet " + (pos.x + 0.3) + " " + (pos.y - 0.5) + " " + (pos.z + 0.5) + " {lifetime:15, destX:" + (pos.x - 0.2) + ",destY:" + (pos.y + 1) + ",destZ:" + (pos.z + 0.5) + ",value:0}")
    }
    else {
        machine.getLevel().spawnParticles("minecraft:flame", false, machine.pos.x + 0.5, machine.pos.y - 0.5625, machine.pos.z + 0.3, 0, 0, 0, 10, 0.001);
        machine.getLevel().spawnParticles("minecraft:flame", false, machine.pos.x + 0.5, machine.pos.y - 0.5625, machine.pos.z + 0.57, 0, 0, 0, 10, 0.001);
    }
});```