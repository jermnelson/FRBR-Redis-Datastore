%rebase layout title="FRBR Redis Datastore Server"
<section>
 <header>
  <h1>Datastore Statistics</h1>
% for stat in ds_stats:
  <p>{{ stat['name'] }} {{ stat['count'] }}</p>
% end
 </header>
</section>
