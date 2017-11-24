



# Architecture

High-level architecture of simple games can be seen via 2 dimensions:
1) Games have multiple modes (menu, world, battle). Solution: state machine.
2) Games have rules and are rendered. Solution: MVC.


## State machine
basic idea
- can transition between modes

pros:
- self-contained modes are easier to debug 
- 

cons:
- how is information passed between modes?


## MVC
basic idea
- each entity (eg player) has a model (game logic) and a view (render)
- view reads model, 
- model completely unaware of view(s)

pros:
- easy to unit test model, run headless, and test AI behavior.
- pygame does not contaminate game logic (eg monsters = [], not LayeredDirty)

cons:
- orthogonal to modes/states. Menu has menu model and menu view.  
- Model can change state before the View finishes rendering a battle animation.
View must have brief animations. 
- main menu mode has very thin model, if any.

